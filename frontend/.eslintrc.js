module.exports = {
  env: {
    node: true,
  },

  extends: [
    "plugin:vue/vue3-essential",
    "eslint:recommended",
    "plugin:vue/vue3-recommended",
    "@vue/prettier",
  ],
  plugins: ["vue"],
};
