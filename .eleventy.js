module.exports = function (eleventyConfig) {
  // Copy assets through
  eleventyConfig.addPassthroughCopy("my-site/src/assets");

  // Watch targets
  eleventyConfig.addWatchTarget("my-site/src/assets/css/");
  eleventyConfig.addWatchTarget("my-site/src/assets/images/");

  // Blog posts collection
  eleventyConfig.addCollection("posts", function (collectionApi) {
    return collectionApi
      .getFilteredByGlob("my-site/src/pages/posts/*.md")
      .reverse();
  });

  // Date filter
  eleventyConfig.addFilter("readableDate", (dateObj) => {
    return new Date(dateObj).toLocaleDateString("en-US", {
      year: "numeric",
      month: "long",
      day: "numeric",
    });
  });

  return {
    dir: {
      input: "my-site/src",
      output: "my-site/dist",
      includes: "components",
      data: "data",
      layouts: "_layouts"
    },
    markdownTemplateEngine: "njk",
    htmlTemplateEngine: "njk"
  };
};