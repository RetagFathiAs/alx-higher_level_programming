#include "lists.h"
#include <stdio.h>
#include <stdlib.h>

/**
 * is_palindrome - Check
 * @head: type listint_s double
 * return: 1 if is a pilndrome 0 if not
 */

int is_palindrome(listint_t **head)
{
	if (head == NULL && *head == NULL)
		return (1);
	else
		return (rec_palindrome(head, *head));
}

/**
 * rec_palindrome - Recursion to check
 * @head: type listint_s double
 * @tail: type listint_s single
 * return: 1 if is a pilndrome 0 if not
 */

int rec_palindrome(listint_t **head, listint_t *tail)
{
	if (tail == NULL)
		return (1);

	if (rec_palindrome(head, tail->next) && (*head)->n == tail->n)
	{
		*head = (*head)->next;
		return (1);
	}
	return (0);
}
