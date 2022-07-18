def post_json(url, payload)
  resp = http.post(
    data=json_of(payload),
    headers=[("Content-Type", "application/json")],
    timeout=45,
    url,
  )
  if resp.status_code() != 200 then
    log(resp)
  end
end

command = "pyponotify --media-id=#{m['schedule_table_id']} &"
command = "pyponotify --webstream='#{json_str}' --media-id=#{!current_dyn_id} &"
command = "pyponotify --error='#{msg}' --stream-id=#{stream} --time=#{!time} &"
command = "pyponotify --connect --stream-id=#{stream} --time=#{!time} &"
command = "pyponotify --source-name=#{sourcename} --source-status=#{status} &"
command = "pyponotify --liquidsoap-started &"
