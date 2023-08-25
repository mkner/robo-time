
Functions
---------

.. py:mod: robo_utils

.. py:function:: robo_utils

 .. py:function:: no indent 1 imap(x, in_min, in_max, out_min, out_max)

  .. py:function:: indent 2 imap(x, in_min, in_max, out_min, out_max)

  .. function:: imap(x, in_min, in_max, out_min, out_max)

.. py:function:: no indent 1 imap(x, in_min, in_max, out_min, out_max)


integer version of fmap
similar to arduino map function (that uses long int numeric types)
but uses the python version of int 



.. py:function:: function(sender, recipient, message_body, [priority=1])

   Send a message to a recipient

   :param str sender: The person sending the message
   :param str recipient: The recipient of the message
   :param str message_body: The body of the message
   :param priority: The priority of the message, can be a number 1-5
   :type priority: integer or None
   :return: the message id
   :rtype: int
   :raises ValueError: if the message_body exceeds 160 characters
   :raises TypeError: if the message_body is not a basestring
