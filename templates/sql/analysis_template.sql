-- =========================================================
-- Daily Project SQL Analysis Template
-- 샘플 분석 포함 (삭제·수정 가능)
--
-- 1) 사용자별 이벤트 개수
-- 2) 시간대별 활동량
-- 3) 세션 기반 기본 집계
-- =========================================================

-- 1) 사용자별 이벤트 개수
SELECT
    user_id,
    COUNT(*) AS total_events
FROM events
GROUP BY user_id
ORDER BY total_events DESC;


-- 2) 시간대별 이벤트 발생량
SELECT
    DATE_TRUNC('hour', event_time) AS hour,
    COUNT(*) AS event_count
FROM events
GROUP BY hour
ORDER BY hour;


-- 3) 세션별 이벤트 수 (feature_store가 있다고 가정)
SELECT
    session_id,
    COUNT(*) AS session_events
FROM session_events
GROUP BY session_id
ORDER BY session_events DESC;


-- =========================================================
--           Fill your code (오늘 분석 내용)
-- =========================================================
