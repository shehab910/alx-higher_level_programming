#include <stdio.h>
#include "lists.h"

/**
 * insert_node - inserts a number into a sorted singly linked list.
 * @head: pointer to pointer of first node of listint_t list
 * @number: integer to be included in new node
 * Return: address of the new element or NULL if it fails
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *new;
	listint_t *current;
	listint_t *prev;

	current = *head;
	prev = NULL;

	new = malloc(sizeof(listint_t));
	if (new == NULL)
		return (NULL);
	new->n = number;
	new->next = NULL;
	if (*head == NULL)
		*head = new;
	else
	{
		while (current != NULL)
		{
			if (current->n > number)
			{
				if (prev == NULL)
				{
					new->next = current;
					*head = new;
				}
				else
				{
					prev->next = new;
					new->next = current;
				}
				break;
			}
			prev = current;
			current = current->next;
		}
		if (current == NULL)
			prev->next = new;
	}
	return (new);
}
