/**
 * Created by linyuchen on 2017/4/18.
 */
/* global __dirname, process */
import path from 'path'
import fs from 'fs'

import HtmlPlugin from 'html-webpack-plugin'
import CONFIG_DEBUG from './src/config/debug'

// 是否调试环境
let DEBUG = process.argv.find((i)=> i === '-p' ) == null;

if (DEBUG !== CONFIG_DEBUG){
    fs.writeFile(path.join(__dirname, "src/config/debug.js"), `export default ${DEBUG ? "true" : "false"}`);
}


const config = {
    context: path.join(__dirname, 'src'),
    entry:{
        "index": ["./app/index.tsx"],
        "backend": ["./app/backend/index.tsx"]
    },
    output:{
        path: path.resolve(__dirname, "build"),
        filename: '[name]-[hash].js'
    },
    resolve: {
        extensions:[".js", ".ts", ".tsx" ]
    },
    module: {

        loaders: [
            {
                test: /\.js$/,
                // exclude: /node_modules/,
                loader:[
                    "babel-loader"
                ]
            },
            {
                test: /\.css$/,
                exclude: /antd/,
                loaders: [
                    'style-loader',
                    'css-loader?module&localIdentName=[name]-[local]-[hash:8]',
                ]
            },

            {
              test: /\.css$/,
              include: /antd/,
              loaders: [
                'style-loader',
                'css-loader',
              ]
            },

            {
                test: /\.tsx?$/,
                loader:[
                    "ts-loader"
                ],
            },

            {
                test: /\.(png|jpg|gif)$/,
                loader: 'url-loader?name=images/[hash:8].[name].[ext]&limit=30000'
            }

        ]
    },
    plugins:[
        // new HtmlPlugin({
        //     publicPath: (DEBUG ? "" : "http://oua8rae54.bkt.clouddn.com/xyj_eb/"),
        //     template: path.resolve(__dirname, "src/tpl/index.html"),
        //     chunks: ["index"],
        //     filename: "index.html"
        // }),
        new HtmlPlugin({
          publicPath: (DEBUG ? "" : "http://oua8rae54.bkt.clouddn.com/xyj_eb/"),
          template: path.resolve(__dirname, "src/tpl/backend.html"),
          chunks: ["backend"],
          filename: "backend.html"
        }),
    ]
};

if (DEBUG) {
    config.devtool = 'inline-source-map';
    config.watch = true;
    config.devServer = {
        disableHostCheck: true,
        inline: true,
        hot: true,
        proxy: {},
    };
    function addProxy(path, host, port) {

        config.devServer.proxy[path] = {
            target: {
                protocol: 'http:',

                host: host,
                port: port,

            },
            secure: false,
            ignorePath: false,
            changeOrigin: true
        }
    }
    var testHost = "localhost";
    var testPort = 8000;
    // var testHost = "weixin.womuji.com.cn";
    // var testPort = 80;
    addProxy("/api", testHost, testPort);
}

export default config;
