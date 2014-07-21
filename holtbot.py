''' HoltBot v. 0.1 - BROCK HOLT!
    Written by Adam Even Engel
    Responds to Brock Holt mentions with a simple \o/
    Seriously, that's it.

    UA string: HoltBot - The ultimate supporter of Red Sox rookie legend Brock Holt. \o/
'''

import time, praw, requests

def holt():
    r = praw.Reddit(user_agent='HoltBot 1.o.1 - The ultimate supporter of Red Sox rookie legend Brock Holt. \o/')
    r.login('holtbot', 'Br0ckH0lt!')
    print "Connected!"
    sifted = set()
    hb_comments = praw.objects.Redditor(r, user_name='holtbot').get_comments(limit=None) # Have to get my own comments to populate set.
    for comment in hb_comments:
        if comment.parent_id[0] =='t':
            sifted.add(comment.parent_id[comment.parent_id.index('_')+1:])
        else:
            sifted.add(comment.parent_id)
    # Wheeee! Time to rewrite to use comment_stream!
    print sifted
    while True:
        try:
            sub = praw.helpers.comment_stream(r, 'redsox+baseball', limit=100)
            for listing in sub: # Now just regularly updating
                if "holtbot" not in str(listing.author).lower():
                    if "brock holt" in listing.body.lower() or "brockholt" in listing.body.lower() and listing.id not in sifted:
                        print "Brock Holt found!"
                        holt_string = '''\o/'''
                        sifted.add(listing.id)
                        comment_poster(holt_string, listing)
                    elif "holt" in listing.body.lower() and listing.id not in sifted:
                        print "Holt found!"
                        holt_string = '''Brock Holt! \o/'''
                        sifted.add(listing.id)
                        comment_poster(holt_string, listing)
        except requests.exceptions.RequestException:
            print "Could not connect. Sleeping for 10 mins."
            time.sleep(300)
    string = "Holts found: %d."%(counter, time.ctime(), len(sifted))
    print string
        
def comment_builder(holt_string):
    footer = '''----- \n This praise brought to you by **HoltBot 1.o.1**.'''
    holt_comment = '''%s \n %s'''%(holt_string, footer)
    return holt_comment
    
def comment_poster(holt_string, listing):
    print "Built comment: %s"%(comment_builder(holt_string))
    try:
        listing.reply(comment_builder(holt_string))
        print "Successfully posted."
    except praw.errors.RateLimitExceeded as e:
        print "Skipping comment %s due to the following error. Will catch on next round. Error: %s"%(listing.id, e)
    
                        
            
if __name__ == '__main__':
    holt()
