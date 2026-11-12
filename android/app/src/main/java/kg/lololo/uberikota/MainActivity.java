package kg.lololo.uberikota;

import android.os.Bundle;
import android.webkit.WebSettings;
import com.getcapacitor.BridgeActivity;

public class MainActivity extends BridgeActivity {

    @Override
    public void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        fixWebView();
    }

    @Override
    public void onResume() {
        super.onResume();
        fixWebView();
    }

    // Крупный шрифт в настройках телефона не должен ломать вёрстку игры
    private void fixWebView() {
        try {
            if (getBridge() != null && getBridge().getWebView() != null) {
                WebSettings s = getBridge().getWebView().getSettings();
                s.setTextZoom(100);
                s.setMediaPlaybackRequiresUserGesture(false);
            }
        } catch (Exception ignored) {}
    }
}
