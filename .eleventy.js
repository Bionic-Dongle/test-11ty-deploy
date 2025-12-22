module.exports = function (eleventyConfig) {
  // Copy assets through
  eleventyConfig.addPassthroughCopy("my-site/src/assets");
  eleventyConfig.addPassthroughCopy({"admin": "admin"});

  // Watch for changes in CSS and images
  eleventyConfig.addWatchTarget("my-site/src/assets/css/");
  eleventyConfig.addWatchTarget("my-site/src/assets/images/");

  // Create blog posts collection
  eleventyConfig.addCollection("posts", function (collectionApi) {
    return collectionApi
      .getFilteredByGlob("my-site/src/pages/posts/*.md")
      .reverse();
  });

  // Add date filter for post dates
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
      layouts: "_layouts",
    },
    markdownTemplateEngine: "njk",
    htmlTemplateEngine: "njk",
  };
};
