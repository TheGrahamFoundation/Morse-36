#!/usr/bin/env node

/**
 * Publish a text update to the David Labs LinkedIn organization page.
 *
 * Required environment variables:
 *   LINKEDIN_ACCESS_TOKEN   OAuth token with w_organization_social
 *   LINKEDIN_ORG_ID         Numeric LinkedIn organization ID
 *
 * Optional:
 *   LINKEDIN_VERSION        LinkedIn Marketing API version (YYYYMM)
 *   LINKEDIN_POST_TEXT      Explicit post body. If omitted, a commit-derived body is used.
 *   GITHUB_REPOSITORY       Supplied automatically by GitHub Actions
 *   GITHUB_SHA              Supplied automatically by GitHub Actions
 */

const token = process.env.LINKEDIN_ACCESS_TOKEN;
const orgId = process.env.LINKEDIN_ORG_ID;
const version = process.env.LINKEDIN_VERSION || "202608";

if (!token) throw new Error("Missing LINKEDIN_ACCESS_TOKEN");
if (!orgId) throw new Error("Missing LINKEDIN_ORG_ID");

const repo = process.env.GITHUB_REPOSITORY || "TheGrahamFoundation/Morse-36";
const sha = process.env.GITHUB_SHA || "";
const shortSha = sha ? sha.slice(0, 7) : "latest";
const commitUrl = sha ? `https://github.com/${repo}/commit/${sha}` : `https://github.com/${repo}`;

const defaultText = [
  "Morse/36 protocol update.",
  "",
  "M36 envelopes are now explicitly self-describing and recursively decodable: anything can be Morsed, and anything Morsed can be re-Morsed. The package tells a compatible decoder how to come back.",
  "",
  "Encoding is not encryption. 36 is an envelope ceiling, not a padding requirement.",
  "",
  `${shortSha} · ${commitUrl}`,
].join("\n");

const commentary = (process.env.LINKEDIN_POST_TEXT || defaultText).trim();
if (!commentary) throw new Error("LinkedIn post text is empty");

const response = await fetch("https://api.linkedin.com/rest/posts", {
  method: "POST",
  headers: {
    Authorization: `Bearer ${token}`,
    "Content-Type": "application/json",
    "X-Restli-Protocol-Version": "2.0.0",
    "Linkedin-Version": version,
  },
  body: JSON.stringify({
    author: `urn:li:organization:${orgId}`,
    commentary,
    visibility: "PUBLIC",
    distribution: {
      feedDistribution: "MAIN_FEED",
      targetEntities: [],
      thirdPartyDistributionChannels: [],
    },
    lifecycleState: "PUBLISHED",
    isReshareDisabledByAuthor: false,
  }),
});

const responseText = await response.text();
if (!response.ok) {
  throw new Error(`LinkedIn publish failed (${response.status}): ${responseText}`);
}

console.log("LinkedIn post published successfully.");
console.log("Post URN:", response.headers.get("x-restli-id") || "not returned");
