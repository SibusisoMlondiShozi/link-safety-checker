import streamlit as st
from checker.validator import is_valid_url
from checker.scorer import score_url

st.set_page_config(page_title="Link Safety Checker", page_icon="🔐")

st.markdown("<h1 style='text-align:center;'>🔐 Link Safety Checker</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align:center;'>Free URL risk analysis using security heuristics</p>", unsafe_allow_html=True)

url = st.text_input("🔗 Enter a URL", placeholder="https://example.com")
scan = st.button("🚀 Scan Link", use_container_width=True)

if scan:
    if not is_valid_url(url):
        st.error("Invalid URL format.")
    else:
        score, verdict, reasons, meta = score_url(url)

        st.divider()
        st.metric("Verdict", verdict)
        st.progress(min(score / 100, 1.0))

        if verdict == "SAFE":
            st.success(f"Score: {score}")
        elif verdict == "SUSPICIOUS":
            st.warning(f"Score: {score}")
        else:
            st.error(f"Score: {score}")

        with st.expander("🔍 Why this result?"):
            for r in reasons:
                st.write("•", r)

        with st.expander("📊 Technical details"):
            st.json(meta)

st.divider()
st.caption("Built by [Sibusiso Shozi](https://sibusisomlondishozi.github.io/smshozi/) • Free & Open Source")
