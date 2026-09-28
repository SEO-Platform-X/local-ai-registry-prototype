import sys,os; sys.path.insert(0,'/tmp/gen'); from headers import *
os.chdir('/mnt/user-data/outputs/artifacts/01ea5720-d0c8-4528-b8cc-76eb1693feae/project')
MAP={'Post.dc.html':doc('Posting','Back to Explore','Explore.dc.html'),'Search.dc.html':doc('Search','Back to home','Home.dc.html'),'Book.dc.html':doc('Booking','Back to Lumen','Main.dc.html'),
 'Notify.dc.html':doc('Notifications','Back to profile','Me.dc.html'),'Moderation.dc.html':doc('Reporting a post','Back to Lumen','Main.dc.html'),
 'AddBiz.dc.html':doc('Add a business','Back to search','Search.dc.html'),'ClaimIssue.dc.html':doc('Claim problems','Back to claim','Claim.dc.html'),'Verify.dc.html':doc('Verify with Google','Back to dashboard','OwnerHome.dc.html'),
 'Invite.dc.html':doc('Team invite','Back to team','OwnerTeam.dc.html'),'Emails.dc.html':doc('Owner emails','Back to dashboard','OwnerHome.dc.html'),'Billing.dc.html':doc('Plan and billing','Back to settings','OwnerSettings.dc.html'),
 'AddLocation.dc.html':doc('Add a location','Back to dashboard','OwnerHome.dc.html'),'RefLanding.dc.html':doc('Referral landing','Back to referral','OwnerReferral.dc.html')}
for f,h in MAP.items():
    s=open(f).read(); open(f,'w').write(swap(s,h))
print('headers applied')
