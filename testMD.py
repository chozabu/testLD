'''
Tests for Simple Liquid representation test for Mesh Democracy
Basic concept is to form a heirachy of groups
Allow for representation in groups
Pass representation into subgroups
'''
import MD

#main function to perform a small test
def main():
  #make topic tree (topic, parent)
  MD.addTopic("science")
  MD.addTopic("physics", "science")
  MD.addTopic("chemistry", "science")
  MD.addTopic("biology", "science")
  
  MD.addTopic("computing")
  MD.addTopic("programming", "computing")
  MD.addTopic("python", "programming")
  MD.addTopic("c++", "programming")
  MD.addTopic("java", "programming")
  
  MD.addTopic("linux", "computing")
  MD.addTopic("GNU", "computing")
  MD.addTopic("windows", "computing")
  MD.addTopic("apple", "computing")
  MD.addTopic("android", "computing")
  
  
  #in science bob represents alice
  MD.selectRepresentitive("science","bob", "alice")
  MD.selectRepresentitive("computing","alex", "alice")
  MD.selectRepresentitive("science","bob", "alice")

  #in physics eve represents bob
  MD.selectRepresentitive("physics","eve","bob")
  MD.selectRepresentitive("programming","alex","bob")
  
  
  MD.selectRepresentitive("python","alex","dave")
  
  
  MD.selectRepresentitive("programming","alex","sara")
  
  
  MD.selectRepresentitive("computing","alex","jane")
  
  
  MD.selectRepresentitive("computing","sara","mike")
  
  
  MD.selectRepresentitive("programming","dave","sally")
  
  
  MD.selectRepresentitive("computing","sally","franko")
  
  
  MD.selectRepresentitive("computing","bob","john")

  #imagine a post in physics where only eve votes
  votes={"alex":1,}

  #or eve and bob
  #votes={"eve":1, "bob":1}

  #or alice
  #votes={"alice":1}

  MD.countVotes("python",votes)


if __name__ == "__main__":
    main()