---
- name: Playbook_Apache
  hosts: 192.168.33.10 #Especifica l'amfitrió on s'executaran les tasques.
  sudo: yes #Executar amb privilegis sudo.

  vars:
    http_port: 80 #Port que s'utilitzarà.
    domain: example.com #Domini d'exemple.

  tasks:
    - name: install apache2 #Utilitza el mòdul apt per instal·lar.
      apt:
       name: apache2
       update_cache: yes
       state: latest
    - name: ensure apache is running #Utilitza el mòdul service per assegurar-se que Apache2 estigui en execució.
      service:
       name: apache2
       state: started
       enabled: yes
    - name: enabled mod_rewrite #Utilitza el mòdul apache2_module per habilitar el mòdul de 'mod_rewrite'.
      apache2_module:
       name: rewrite
       state: present
      notify: restart apache2
    - name: apache2 listen on port {{ http_port }} #Utilitza el mòdul lineinfile perquè Apache escolti el port 'http_port'.
      lineinfile: dest=/etc/apache2/ports.conf regexp="^Listen " line="Listen {{ http_port }}" state=present
      notify: restart apache2
    - name: create virtual host file #Utilitza el mòdul template per copiar un fitxer de configuració 'virtualhost.conf'.
      template: src=/tmp/virtualhost.conf dest=/etc/apache2/sites-available/{{ domain }}.conf
      notify: restart apache2

  handlers:
    - name: restart apache2 #Defineix un manipulador que reinicia el servei d'Apache.
      service:
       name: apache2
       state: restarted
