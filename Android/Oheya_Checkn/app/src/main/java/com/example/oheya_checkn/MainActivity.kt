package com.example.oheya_checkn

import androidx.appcompat.app.AppCompatActivity
import android.os.Bundle
import android.webkit.WebView
import android.webkit.WebViewClient

class MainActivity : AppCompatActivity() {

    // 画面表示WebView
    private var mWebView: WebView? = null


    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_main)

        // 画面のインスタンスを取得
        mWebView = findViewById(R.id.webView) as WebView

        // WebSettingsオブジェクトを取得
        val settings = mWebView!!.settings

        // JavaScriptを有効にする
        settings.javaScriptEnabled = true

        // WebViewのリンクをクリックするたびにIntentが発行される処理を無効にする
        mWebView!!.setWebViewClient(WebViewClient())

        // 起動時にOheya_Checknを読み込む
        if (savedInstanceState == null) {
            mWebView!!.loadUrl("https://github.com/tak-st/oheya_checkn/pulls")
        } else {
            // WebViewの状態を復元
            mWebView!!.restoreState(savedInstanceState)
        }

    }
    override fun onSaveInstanceState(outState: Bundle) {
        // WebViewの状態を保存する（画面の回転前の状態を保存する処理）
        mWebView!!.saveState(outState)
        super.onSaveInstanceState(outState)
    }


    override fun onBackPressed() {
        // 履歴があれば、Backキーで前のページヘ戻る
        if (mWebView!!.canGoBack()) {
            mWebView!!.goBack()
        } else {
            // 履歴がなければ通常通りBackキーの処理を行い、Activityを終了する
            super.onBackPressed()
        }
    }

    override fun onPause() {
        super.onPause()
        // WebViewで実行中の処理を停止
        mWebView!!.onPause()
    }

    override fun onResume() {
        // WebViewの処理を再び開始
        mWebView!!.onResume()
        super.onResume()
    }

    override fun onDestroy() {
        // WebViewを安全に終了
        if (mWebView != null) {
            mWebView!!.stopLoading()
            mWebView!!.setWebChromeClient(null)
            mWebView!!.setWebViewClient(null)
            mWebView!!.destroy()
            mWebView = null
        }
        super.onDestroy()
    }

}