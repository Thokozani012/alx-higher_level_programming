#include <stdio.h>
#include <stdlib.h>
#include "lists.h"

/**
  * insert_node - Inserts a new node on a sorte
  * @head: pointer to the head of the list
  * @number: number/value to the inserted into the sorted list
  *
  * Return: The address of th new node
  */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *prev;
	listint_t *curr;
	listint_t *new;

	curr = *head;

	/*memory allocatio for the new node*/
	new = malloc(sizeof(listint_t));
	if (new == NULL)
	{
		return (NULL);
	}

	new->n = number;
	new->next = NULL;

	if (*head == NULL || number <= (*head)->n)
	{
		new->next = *head; /*here head is pointing to NULL*/
		*head = new;
		return (new);
	}

	while (curr != NULL && number > curr->n)
	{
		prev = curr;
		curr = curr->next;
	}

	/*insert the node here-> number <= curr->n*/
	prev->next = new;
	new->next = curr;

	return (new);
}
