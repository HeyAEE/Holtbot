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
    counter = 0
    subs_to_scan = ['redsox', 'baseball']
    
    while True:
        counter += 1
        for entry in subs_to_scan:
            try:
                sub = r.get_subreddit(entry)
                print "Subreddit results: "+str(sub)
                for listing in list(sub.get_comments()): # Pulls 200 most recent comments from multisub
                    if "brock holt" in listing.body.lower() or "brockholt" in listing.body.lower() and listing.id not in sifted:
                        print "Brock Holt found!"
                        holt_string = '''\o/'''
                        sifted = comment_poster(holt_string, listing, sifted)
                    elif "holt" in listing.body.lower() and listing.id not in sifted:
                        print "Holt found!"
                        holt_string = '''Brock Holt! \o/'''
                        sifted = comment_poster(holt_string, listing, sifted)
            except requests.exceptions.RequestException:
                print "Could not connect. Sleeping for 10 mins."
        string = "Scan %d run on %s. Holts found: %d."%(counter, time.ctime(), len(sifted))
        print string
        time.sleep(600)
        
def comment_builder(holt_string):
    footer = '''----- \n This praise brought to you by **HoltBot 1.o.1**.'''
    holt_comment = '''%s \n %s'''%(holt_string, footer)
    return holt_comment
    
def comment_poster(holt_string, listing, sifted):
    print "Built comment: %s"%(comment_builder(holt_string))
    try:
        listing.reply(comment_builder(holt_string))
        print "Successfully posted."
        sifted.add(listing.id)
        return sifted
    except praw.errors.RateLimitExceeded as e:
        print "Skipping comment %s due to the following error. Will catch on next round. Error: %s"%(listing.id, e)
    
                        
            
if __name__ == '__main__':
    holt()
