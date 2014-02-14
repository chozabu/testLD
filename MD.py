'''
Simple Liquid representation test for Mesh Democracy
Basic concept is to form a heirachy of groups
Allow for representation in groups
Pass representation into subgroups
'''
import time
#3 people in this test - bob knows alice and eve. alice and eve do not know each other.
#people = {"alice":{}, "bob":{}, "eve":{}}

#simple dict of topics
topicDict = {}

#store a representation with timestamp
def selectRepresentitive(topic, representer, representee):
  topicReps = topicDict[topic]["reps"]
  if representee not in topicReps:topicReps[representee]={}
  topicReps[representee]["representer"]= representer;
  topicReps[representee]["timestamp"]= time.time();

#recursive function to get all representees of a voter using the "topic tree"
#could do with optimisation and clarification
def getRepVotes(voter, topic):
  print "getRepVotes(",voter, ",",topic,")"
  topicScore=0
  
  if "parent" in topicDict[topic]:
    topicScore+=getRepVotes(voter, topicDict[topic]["parent"])
  #print topicDict[topic]
  topicReps = topicDict[topic]["reps"]
  for representee in topicReps:
    if representee in liquidVoted:
      pass
      #print "Representee: "+representee+" already counted, skipping (check timestamps?)"
    else:
      if representee not in directVoted:
        representer = topicReps[representee]["representer"]
        if representer == voter:
          topicScore+=1
          liquidVoted[representee]=True
          if "parent" in topicDict[topic]:
            topicScore+=getRepVotes(representee, topicDict[topic]["parent"])
  return topicScore

directVoted={}#dict of people who have already voted directly
liquidVoted={}#dict of people who have been counted as a representee

#get result of liquid votes
def countVotes(vTopic,tVotes):
  #reset for recount
  directVoted={}
  liquidVoted={}
  directscore = 0
  liquidscore = 0
  
  #count direct votes
  for v in tVotes:
    directscore+=tVotes[v]
    directVoted[v]=True
  print "directscore",directscore
  
  #count representees recursivly
  for v in tVotes:
    liquidscore+=getRepVotes(v, vTopic)
  print "liquidscore",liquidscore
    
  print "FINALSCORE",directscore+liquidscore
  
def clearTopics():
  topicDict = {}
  
def addTopic(key, parent=None):
  topicDict[key] = {"reps":{}}
  if parent:
    topicDict[key]["parent"] = parent
  


#main function to perform a small test
def main():
  #make topic tree (topic, parent)
  addTopic("science")
  addTopic("physics", "science")
  
  #in science bob represents alice
  selectRepresentitive("science","bob", "alice")

  #in physics eve represents bob
  selectRepresentitive("physics","eve","bob")

  #imagine a post in physics where only eve votes
  votes={"eve":1,}

  #or eve and bob
  #votes={"eve":1, "bob":1}

  #or alice
  #votes={"alice":1}

  countVotes("physics",votes)


if __name__ == "__main__":
    main()