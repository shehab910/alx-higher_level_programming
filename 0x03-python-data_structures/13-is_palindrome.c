#include "lists.h"

/**
reverse_linked_list - Reverses a singly-linked listint_t list.
@head: A pointer to the starting node of the list to reverse.
Return: A pointer to the head of the reversed list.
*/
listint_t *reverse_linked_list(listint_t **head)
{
	listint_t *node = *head, *next, *prevNode = NULL;

	while (node)
	{
		next = node->next;
		node->next = prevNode;
		prevNode = node;
		node = next;
	}

	*head = prevNode;
	return (*head);
}

/**
is_palindrome - Checks if a singly linked list is a palindrome.
@head: A pointer to the head of the linked list.
Return: If the linked list is not a palindrome - 0.
	If the linked list is a palindrome - 1.
*/
int is_palindrome(listint_t **head)
{
	listint_t *tmp, *reversedHead, *mid;
	size_t size = 0, i;

	if (*head == NULL || (*head)->next == NULL)
		return (1);

	tmp = *head;
	while (tmp)
	{
		size++;
		tmp = tmp->next;
	}

	tmp = *head;
	for (i = 0; i < (size / 2) - 1; i++)
		tmp = tmp->next;

	if ((size % 2) == 0 && tmp->n != tmp->next->n)
		return (0);

	tmp = tmp->next->next;
	reversedHead = reverse_linked_list(&tmp);
	mid = reversedHead;

	tmp = *head;
	while (reversedHead)
	{
		if (tmp->n != reversedHead->n)
			return (0);
		tmp = tmp->next;
		reversedHead = reversedHead->next;
	}
	reverse_linked_list(&mid);

	return (1);
}