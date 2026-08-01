#include "lists.h"
#include <stddef.h>

/**
 * check_palindrome - recursively checks if a list is a palindrome
 * @left: pointer to the left side pointer
 * @right: current node from the right side
 *
 * Return: 1 if palindrome, 0 otherwise
 */
int check_palindrome(listint_t **left, listint_t *right)
{
	if (right == NULL)
		return (1);

	if (!check_palindrome(left, right->next))
		return (0);

	if ((*left)->n != right->n)
		return (0);

	*left = (*left)->next;

	return (1);
}

/**
 * is_palindrome - checks if a singly linked list is a palindrome
 * @head: pointer to the head pointer
 *
 * Return: 1 if palindrome, 0 otherwise
 */
int is_palindrome(listint_t **head)
{
	if (head == NULL || *head == NULL)
		return (1);

	return (check_palindrome(head, *head));
}
