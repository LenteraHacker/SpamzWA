�
��]c        	   @   s�   d  d l  Z  d  d l Z d  d l Z d  d l Z d  d l Z e  j �  Z d Z d Z d Z	 d e e	 e e	 e e	 e e	 f Z
 d d d �  �  YZ e j e �  � d S(	   i����Ns   [91ms   [96ms   [0ms�   
  SPAM WHATSAPP 2019
%s >>>>>>>>>>>>>>>>>>>>>>>>>>>>>
 > %scode : DW             %s>
 > %stype : wa/email             %s>
 > %steam : Eagle Anonymous             %s>
 >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>%s
    t
   Mate_lampuc           B   s#   e  Z d  �  Z d �  Z d �  Z RS(   c         C   s;   t  d � j �  j �  |  _ t j d � t GH|  j �  d  S(   Ns   ua.txtt   clear(   t   opent   readt
   splitlinest   uat   ost   systemt
   __banner__t   sok_aelu(   t   self(    (    s
   kitabis.pyt   __init__   s    
c         C   s�   t  t d � � } | d k r? d |  _ t  t d � � |  _ n4 | d k rl d |  _ t  t d � � |  _ n t �  |  j �  d  S(   Ns
   [?] type: t   wat   phone_numbers   [?] no wa: t   emails   [?] email: (   t   strt   inputt   tololt   goblokR    t   spam_kuy(   R
   t   type(    (    s
   kitabis.pyR	      s    		c         C   s  t  t d � � } d GHx� t d | d � D]� } t j j i t j |  j � d 6� t j	 d d i d d 6|  j
 d	 6|  j d
 6�} | j d k r� d t
 | t f GHn+ d
 t
 | t | j �  d d d d f GHt j d � q+ q+ Wt d t t t t
 f � d  S(   Ns   [?] jumlh: s6   [!] delay 30 detik untuk dapat melancarkan proses spami   s
   user-agents.   https://core.ktbs.io/v2/user/registration/tempt   jsont   Maoundist	   full_namet   user_idt   user_id_typei�   s      %s[%d] pesan: %sSPAM BERHASIL s     %s[%d] pesan: %s%st   errorsi    t   detailst   idi�   s   %s[%s#%s]%s SELESAI EXIT ,,,,(   t   intR   t   ranget   reqt   headerst   updatet   randomt   choiceR   t   postR   R   t   status_codet   wt   ct   rR   t   timet   sleept   quit(   R
   t   saapat   it   ceko(    (    s
   kitabis.pyR   (   s    # 0+
(   t   __name__t
   __module__R   R	   R   (    (    (    s
   kitabis.pyR       s   		(    (
   t   requestsR"   R)   R   t   syst   SessionR   R(   R'   R&   R   R    t   exit(    (    (    s
   kitabis.pyt   <module>   s   <	")
