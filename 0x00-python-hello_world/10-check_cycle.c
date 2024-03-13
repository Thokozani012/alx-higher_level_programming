#include <stdio.h>
#include <stdlib.h>
#include "lists.h"

/**
  * check_cycle - Checks if a singly linked list has a cycle
  * @list: singl linked list
  *
  * Return: 0 is there is no cycle, or 1 if there is a cyle
  */
int check_cycle(listint_t *list)
{
	listint_t *fast_ptr = list, *slow_ptr = list;

	if (list == NULL)
	{
		return (0);
	}

	while (slow_ptr && fast_ptr && fast_ptr->next)
	{
		slow_ptr = slow_ptr->next;
		fast_ptr = fast_ptr->next->next;

		if (slow_ptr == fast_ptr)
		{
			return (1);
		}
	}

	return (0);
}
