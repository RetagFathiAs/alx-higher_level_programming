#include "lists.h"

/**
 * is_palindrome - Check is the listint is a Palindrome
 * @head: type listint_s double pointer of node
 * return: 1 if is a pilndrome 0 if not
 */

int is_palindrome(listint_t **head)
{
        if (head == NULL && *head == NULL)
            return (1);
        else
            return (check_p(head, *head));
}
 /**
 * check_p - Recursion to check each node as palindrome
 * @head: type listint_s double pointer of node
 * @tail: type listint_s single pointer of last node
 * return: 1 if is a pilndrome 0 if not
 */
int check_p(listint_t **head, listint_t *tail)
{
        if (tail == NULL)
                return (1);
        if (check_p(head, tail->next) && (*head)->n == tail->n)
        {
              *head = (*head)->next;
              return (1);
        }
        return (0);
}
