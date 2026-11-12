# Убери кота 🐱

Уютная головоломка для Android: укладывай пледы, собирай ряды и отправляй котиков спать.

- Игра: `src/game.html` (один файл, Canvas + WebAudio, без библиотек)
- Сборка веб-файла со шрифтами: `python3 tools/build.py` → `www/index.html`
- Android-обёртка: Capacitor 8 (`android/`), реклама: `@capacitor-community/admob`
- Сборка AAB/APK: GitHub Actions (`.github/workflows/android.yml`); готовые файлы появляются в ветке `builds`
- Тексты и графика для Google Play: папка `store/`
- Политика конфиденциальности: [PRIVACY.md](PRIVACY.md)

## Реклама AdMob
Сейчас стоят **тестовые** ID Google. Перед выпуском замените:
1. `android/app/src/main/res/values/strings.xml` → `admob_app_id` (ID приложения `ca-app-pub-…~…`)
2. `src/game.html` → объект `ADCFG`: `banner`, `interstitial`, `rewarded` (ID рекламных блоков `ca-app-pub-…/…`) и `test:false`
3. Увеличьте `versionCode` в `android/app/build.gradle`, запустите `tools/build.py`, закоммитьте.

Ключ подписи (`upload keystore`) в репозитории **не хранится**.
