-- 코드를 입력하세요
SELECT book_id, TO_CHAR(PUBLISHED_DATE,'YYYY-MM-DD') as PUBLISHED_DATE
FROM book
WHERE category = '인문' AND TO_CHAR(published_date, 'YYYY') = '2021'
ORDER BY published_date