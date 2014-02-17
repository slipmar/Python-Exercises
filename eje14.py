def removingItems(elements):

	if len(elements)==0 or len(elements)==1 or len(elements)==2 or len(elements)==3:
		empty = []
		return empty
	else:
		begin = elements[0]
		middle = elements[len(elements)/2]
		end = elements[len(elements)-1]

		elements.remove(begin)
		elements.remove(middle)
		elements.remove(end)
		return elements
