"""
1. self
2. child
3. parent

4. descendant
5. following
6. following-sibling

7. ancestor
8. preceding
9. preceding-sibling
"""
# syntax: xpath_expression/axis_func::tag_name

"""
1. self
-------
//h3[text()="Parent - Electronics"]
//h3[text()="Parent - Electronics"]/self::h3

2. parent
---------
//h3[text()="Parent - Electronics"]/..
//h3[text()="Parent - Electronics"]/parent::div
//h3[text()="Parent - Electronics"]/parent::*

3. child
--------
//div[@id="parent1"]/p
//div[@id="parent1"]/*

//div[@id="parent1"]/child::p
//div[@id="parent1"]/child::*

4. following - all the tags present after the located one(the located
-------------- elements hierarchy will not be considered)

//div[@id="parent1"]/following::li  -> 5 matches leaving li tags inside parent1

5. following-sibling
--------------------
//h3[text()="Parent - Clothing"]/following-sibling::ol
//h3[text()="Parent - Clothing"]/following-sibling::*

6. preceding - all the tags before the located tag will be selected
-------------
 //div[@id="child3-2"]/preceding::*

7. preceding-sibling -
----------------------
//div[@id="child3-2"]/preceding-sibling::h3
//div[@id="child3-2"]/preceding-sibling::*

8. ancestor - parent/grand parent/great grand parent
------------
//div[@id="child3-2"]/ancestor::div
//div[@id="child3-2"]/ancestor::*

9. descendant - child/grandchild/great grandchild
-------------
//div[@id="nestedParent"]/descendant::*

10. attribute
--------------
//div[@id="nestedParent"]
//div[attribute::id="nestedParent"]

"""





