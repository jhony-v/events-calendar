const path = require("path");
const MiniCSSExtractPlugin = require("mini-css-extract-plugin");

const entryJs = (filename) => [
  `./src/js/${filename}.js`,
  `./src/scss/${filename}.scss`,
];

module.exports = {
  entry: {
    home: entryJs("home"),
    events: entryJs("events"),
    profile: entryJs("profile"),
    settings: entryJs("settings"),
    tags: entryJs("tags"),
    reset : "./src/scss/lib/reset.scss"
  },
  output: {
    path: path.join(__dirname, "static", "js"),
    filename: "[name].bundle.js",
  },
  resolve: {
    extensions: [".ts", ".js"],
  },
  module: {
    rules: [
      {
        test: /\.scss/i,
        use: [MiniCSSExtractPlugin.loader, "css-loader", "sass-loader"],
      },
      {
        test: /\.ts$/,
        use: "ts-loader",
        exclude: /node_modules/,
      },
    ],
  },
  plugins: [
    new MiniCSSExtractPlugin({
      filename: "../css/[name].css",
    }),
  ],
};
