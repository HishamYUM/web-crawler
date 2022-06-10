
import sys
import requests
import lxml
from urllib.parse import urlparse
from bs4 import BeautifulSoup
import argparse
from prettytable import PrettyTable

    



test = ["https://www.cnpp.com/groupsite/career/application/offer/0"]




headers = {"User-Agent": "Mozilla/5.0 (X11; Linux x86_64; rv:101.0) Gecko/20100101 Firefox/101.0"}



def links_with_404error(links):
    error_404 = []
    for l404 in links:
        try:    
            code = requests.get(l404, headers=headers).status_code
            if code == 404:        
                error_404.append(l404)
        except:
            pass

    return error_404


def links_with_form(links):
    links_with_forms = []
    for l_form in links:
        
        try:
            res = requests.get(l_form, headers=headers)
            soup = BeautifulSoup(res.content,'lxml')
            links_f = soup.find('form')
        
            if links_f != None:
                links_with_forms.append(l_form)
        except:
            pass
    return links_with_forms

def links_in_same_domain(url, links):
    same_domain = []
    for l in links:
        l = l['href']
        if l.startswith('/'):
            same_domain.append(url+l)
    return same_domain

def links_protected(links):
    
    protected = []
    logins = ["login", "signin", "my_account", "myaccount", "my-account", "auth",    "se-connecter", "connecter", "connect", "connexion", "identification", "identifier"]
    for protected_l in links:
        for login in logins:
            if login in protected_l:
                protected.append(protected_l)
    return protected

def links_external_domain(domain, links):
    external_domain = []
    for l in links:
        
        l = l['href']
        if "http" in l and domain not in l :
            external_domain.append(l)
    return external_domain


def unique_links(i_links, e_links):
    i_links.extend(e_links)
    unique_links = set(i_links)
    return list(unique_links)


def column_pad(*columns):
    max_len = max([len(c) for c in columns])
    for c in columns:
        c.extend(['']*(max_len-len(c)))
