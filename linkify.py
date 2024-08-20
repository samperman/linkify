from linkify_it import LinkifyIt

def run(input):
  linkify = LinkifyIt()
  match = linkify.match(input)
  if len(match) > 0:
    return match[0].url
  return ""
