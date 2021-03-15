mkdir -p ~/.streamlit/

echo "\
[general]\n\
email = \"asd890123@sina.cn\"\n\
" > ~/.streamlit/credentials.toml

echo "\
[server]\n\
headless = true\n\
enableCORS=false\n\
port = $PORT\n\
" > ~/.streamlit/config.toml
