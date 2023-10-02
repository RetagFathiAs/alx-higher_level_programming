#include "lists.h"
#include <stdlib.h>

/**
 * check_cycle - check for the loop
 * @list: data type
 * Return: 0 if no cycle or 1 if there is a cycle
 */
int check_cycle(listint_t *list)
{
	listint_t *first_arg;
	listint_t *second_arg;

	if (list == NULL || list->next == NULL)
		return  (0);

	first_arg = list->next;
	second_arg = list->next->next;

	while (first_arg && second_arg && second_arg->next)
	{
		if (first_arg == second_arg->next)
		{
			return (1);
		}
		first_arg = first_arg->next;
		second_arg = second_arg->next->next;
	}
	return (0);
}
