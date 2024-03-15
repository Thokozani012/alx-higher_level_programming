#include <stdio.h>
#include <stdlib.h>
#include "lists.h"

/**
  * rev_list - reverses the singly linked list
  * @node: node on th list
  *
  * Return: pointer to the previous node
  */
listint_t *rev_list(listint_t *node)
{
	listint_t *prev = NULL, *curr = node, *Next = NULL;

	while (curr != NULL)
	{
		Next = curr->next;
		curr->next = prev;

		prev = curr;
		curr = Next;
	}

	return (prev);
}

/**
  * is_palindrome - checks whether the given linked list is a palindrome
  * @head: pointer(double) to the singly linked list
  *
  * Return: 0 if the list is NOT a palindrome, or 1 if the list is a palindrome
  */
int is_palindrome(listint_t **head)
{
	listint_t *slow, *fast, *first_half, *second_half;

	if (*head == NULL || (*head)->next == NULL)
	{
		return (1);
	}

	slow = *head;
	fast = *head;

	/*finding the middle of the list*/
	while (fast->next != NULL && fast->next->next != NULL)
	{
		slow = slow->next;
		fast = fast->next->next;
	}

	/*reversing the second half of the linked list*/
	second_half = rev_list(slow->next);

	/*compare the first and second halves*/
	first_half = *head;
	while (second_half != NULL)
	{
		if (first_half->n != second_half->n)
		{
			return (0);
		}
		first_half = first_half->next;
		second_half = second_half->next;
	}

	return (1);
}
