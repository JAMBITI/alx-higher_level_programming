#include "lists.h"

/**
 * check_cycle - checks if a singly linked list has a cycle in it
 * @head: pointer to the head of the list
 * Return: 1 if there is a cycle, 0 otherwise
 */
int check_cycle(listint_t *head)
{
listint_t *slow_ptr, *fast_ptr;

if (!head)
return (0);

slow_ptr = head;
fast_ptr = head->next;

while (fast_ptr && fast_ptr->next)
{
if (slow_ptr == fast_ptr)
return (1);

slow_ptr = slow_ptr->next;
fast_ptr = fast_ptr->next->next;
}

return (0);
}
