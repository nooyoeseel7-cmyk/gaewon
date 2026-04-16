import streamlit as st

st.title("✨ MBTI 맞춤 음악 추천")

# MBTI 선택
mbti = st.selectbox("당신의 MBTI를 선택하세요.", 
                    ["INTJ (전략가)", "ENFP (활동가)", "ISTJ (현실주의자)", "ESFP (연예인)"])

# 추천 버튼
if st.button("내 성격에 맞는 음악은?"):
    st.divider() # 구분선
    
    # 1. INTJ 예시
    if "INTJ" in mbti:
        st.subheader("🧠 냉철한 지성의 전략가, INTJ")
        st.info("당신은 깊은 집중력과 독립적인 사고를 즐깁니다. 복잡한 구조의 클래식이나 차분한 로파이(Lo-fi)가 어울려요.")
        st.success("🎵 추천곡: **Chopin - Nocturne op.9 No.2**")
    
    # 2. ENFP 예시
    elif "ENFP" in mbti:
        st.subheader("🌈 재기발랄한 활동가, ENFP")
        st.info("당신은 창의적이고 자유로운 영혼입니다. 에너지가 넘치고 밝은 멜로디의 팝이나 인디 음악이 딱이에요!")
        st.success("🎵 추천곡: **Harry Styles - Adore You**")

    # 3. 기타 예시 (나머지는 학생들에게 채워보라고 유도하기 좋습니다)
    else:
        st.subheader(f"💫 {mbti}를 위한 추천")
        st.info("당신의 성향을 분석 중입니다... 당신의 고유한 바이브를 응원합니다!")
        st.success("🎵 추천곡: **당신이 가장 좋아하는 노래가 오늘의 정답입니다.**")
