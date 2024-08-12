CREATE TABLE parents AS
  SELECT "abraham" AS parent, "barack" AS child UNION
  SELECT "abraham"          , "clinton"         UNION
  SELECT "delano"           , "herbert"         UNION
  SELECT "fillmore"         , "abraham"         UNION
  SELECT "fillmore"         , "delano"          UNION
  SELECT "fillmore"         , "grover"          UNION
  SELECT "eisenhower"       , "fillmore";

CREATE TABLE dogs AS
  SELECT "abraham" AS name, "long" AS fur, 26 AS height UNION
  SELECT "barack"         , "short"      , 52           UNION
  SELECT "clinton"        , "long"       , 47           UNION
  SELECT "delano"         , "long"       , 46           UNION
  SELECT "eisenhower"     , "short"      , 35           UNION
  SELECT "fillmore"       , "curly"      , 32           UNION
  SELECT "grover"         , "short"      , 28           UNION
  SELECT "herbert"        , "curly"      , 31;

CREATE TABLE sizes AS
  SELECT "toy" AS size, 24 AS min, 28 AS max UNION
  SELECT "mini"       , 28       , 35        UNION
  SELECT "medium"     , 35       , 45        UNION
  SELECT "standard"   , 45       , 60;


-- All dogs with parents ordered by decreasing height of their parent
CREATE TABLE by_parent_height AS
  SELECT child FROM parents,dogs WHERE parent=name ORDER BY height DESC;


-- The size of each dog
CREATE TABLE size_of_dogs AS
  SELECT name AS name,size FROM dogs,sizes WHERE height>min AND height<=max;


-- Filling out this helper table is optional
CREATE TABLE siblings AS
  SELECT a.child AS siblings_A,b.child AS siblings_B FROM parents AS a,parents AS b WHERE a.parent=b.parent AND a.child!=b.child AND a.child<b.child;

-- Sentences about siblings that are the same size
CREATE TABLE sentences AS
  SELECT "The two siblings, " || s.siblings_A || " and " || s.siblings_B || ", have the same size: " || a.size
  FROM siblings AS s,size_of_dogs AS a,size_of_dogs AS b WHERE s.siblings_A=a.name AND s.siblings_B=b.name AND a.size=b.size;


-- Height range for each fur type where all of the heights differ by no more than 30% from the average height
CREATE TABLE low_variance AS
  SELECT fur,(MAX(height)-MIN(height)) FROM dogs GROUP BY fur HAVING (MAX(height))<=(1.3*AVG(height)) AND (MIN(height))>=(0.7*AVG(height));

