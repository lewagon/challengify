SELECT
  -- $ERASE_BEGIN
  movies.minutes / 30 * 30 + 30 as bucket,
  count(*)
  -- $ERASE_END
FROM movies
-- $ERASE_BEGIN
WHERE movies.minutes IS NOT NULL
GROUP BY bucket
ORDER BY bucket
-- $ERASE_END
