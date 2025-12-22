module.exports = function (eleventyConfig) {
  // Copy assets through (adjusted paths since input is now root)
  eleventyConfig.addPassthroughCopy("my-site/src/assets");

  // Watch targets (adjusted)
  eleventyConfig.addWatchTarget("my-site/src/assets/css/");
  eleventyConfig.addWatchTarget("my-site/src/assets/images/");

  // Blog posts collection (adjusted glob)
  eleventyConfig.addCollection("posts", function (collectionApi) {
    return collectionApi
      .getFilteredByGlob("my-site/src/pages/posts/*.md")
      .reverse();
  });

  // Date filter stays the same
  eleventyConfig.addFilter("readableDate", (dateObj) => {
    return new Date(dateObj).toLocaleDateString("en-US", {
      year: "numeric",
      month: "long",
      day: "numeric",
    });
  });

  return {
    dir: {
      input: ".",                         // Root of project
      output: "_site",
      includes: "my-site/src/components",
      data: "my-site/src/data",
      layouts: "my-site/src/_layouts",
    },
    markdownTemplateEngine: "njk",
    htmlTemplateEngine: "njk",
  };
};