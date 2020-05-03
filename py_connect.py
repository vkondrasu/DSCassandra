from cassandra.cluster import Cluster
cluster = Cluster(protocol_version = 3)
session = cluster.connect('killrvideo')

print('{0:12} {1:40} {2:5}'.format('Tag', 'ID', 'Title'))
for val in session.execute("select * from videos_by_tag"):
   print('{0:12} {1:40} {2:5}'.format(val[0], val[2], val[3]))

session.execute(""" INSERT INTO videos_by_tag (tag, video_id, added_date, title) 
VALUES ('venkat_kondrasu', uuid(), toUnixTimestamp(now()), 'my cassandra video') """);

print('{0:12} {1:40} {2:5}'.format('Tag', 'ID', 'Title'))
for val in session.execute("select * from videos_by_tag"):
   print('{0:12} {1:40} {2:5}'.format(val[0], val[2], val[3]))

session.execute(""" DELETE FROM videos_by_tag WHERE tag='venkat_kondrasu' """);

print('{0:12} {1:40} {2:5}'.format('Tag', 'ID', 'Title'))
for val in session.execute("select * from videos_by_tag"):
   print('{0:12} {1:40} {2:5}'.format(val[0], val[2], val[3]))

session.execute(""" INSERT INTO videos_by_tag (tag, video_id, added_date, title) 
VALUES ('cassandra', uuid(), toUnixTimestamp(now()), 'cassandra certification video') """);