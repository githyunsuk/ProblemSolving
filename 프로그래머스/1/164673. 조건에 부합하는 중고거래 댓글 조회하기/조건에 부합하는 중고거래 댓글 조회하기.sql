SELECT ugb.title, ugb.board_id, ugr.reply_id, ugr.writer_id, ugr.contents, ugr.created_date
FROM used_goods_board ugb
JOIN used_goods_reply ugr
  ON ugb.board_id = ugr.board_id
WHERE ugb.created_date between '2022-10-01' and '2022-10-31'
ORDER BY ugr.created_date, ugb.title
