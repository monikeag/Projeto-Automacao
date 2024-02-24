{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "metadata": {},
   "outputs": [],
   "source": [
    "# pip install selenium pyperclip webdriver-manager (Já instalei)\n",
    "from selenium import webdriver\n",
    "from selenium.webdriver.chrome.service import Service\n",
    "from webdriver_manager.chrome import ChromeDriverManager\n",
    "from time import sleep\n",
    "\n",
    "\n",
    "#Parte que faz o site abrir no WhatsApp Web\n",
    "service = Service(ChromeDriverManager().install())\n",
    "nav = webdriver.Chrome(service=service)\n",
    "nav.get(\"https://web.whatsapp.com\")\n",
    "sleep(300)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 1,
   "metadata": {},
   "outputs": [
    {
     "ename": "NameError",
     "evalue": "name 'nav' is not defined",
     "output_type": "error",
     "traceback": [
      "\u001b[1;31m---------------------------------------------------------------------------\u001b[0m",
      "\u001b[1;31mNameError\u001b[0m                                 Traceback (most recent call last)",
      "Cell \u001b[1;32mIn[1], line 10\u001b[0m\n\u001b[0;32m      7\u001b[0m lista_contatos \u001b[38;5;241m=\u001b[39m [\u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mNivea Mana Love\u001b[39m\u001b[38;5;124m\"\u001b[39m, \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mPriscila Prisgay\u001b[39m\u001b[38;5;124m\"\u001b[39m, \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mGlauco Silva\u001b[39m\u001b[38;5;124m\"\u001b[39m]\n\u001b[0;32m      9\u001b[0m \u001b[38;5;66;03m#clicar na lupa\u001b[39;00m\n\u001b[1;32m---> 10\u001b[0m \u001b[43mnav\u001b[49m\u001b[38;5;241m.\u001b[39mfind_element(\u001b[38;5;124m'\u001b[39m\u001b[38;5;124mxpath\u001b[39m\u001b[38;5;124m'\u001b[39m, \u001b[38;5;124m'\u001b[39m\u001b[38;5;124m//*[@id=\u001b[39m\u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mside\u001b[39m\u001b[38;5;124m\"\u001b[39m\u001b[38;5;124m]/div[1]/div/div[2]/button/div[2]/span\u001b[39m\u001b[38;5;124m'\u001b[39m)\u001b[38;5;241m.\u001b[39mclick()\n\u001b[0;32m     11\u001b[0m \u001b[38;5;66;03m#escreve na lupa\u001b[39;00m\n\u001b[0;32m     12\u001b[0m nav\u001b[38;5;241m.\u001b[39mfind_element(\u001b[38;5;124m'\u001b[39m\u001b[38;5;124mxpath\u001b[39m\u001b[38;5;124m'\u001b[39m, \u001b[38;5;124m'\u001b[39m\u001b[38;5;124m//*[@id=\u001b[39m\u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mside\u001b[39m\u001b[38;5;124m\"\u001b[39m\u001b[38;5;124m]/div[1]/div/div[2]/div[2]/div/div[1]/p\u001b[39m\u001b[38;5;124m'\u001b[39m)\u001b[38;5;241m.\u001b[39msend_keys(\u001b[38;5;124m'\u001b[39m\u001b[38;5;124mNivea Mana Love\u001b[39m\u001b[38;5;124m'\u001b[39m)\n",
      "\u001b[1;31mNameError\u001b[0m: name 'nav' is not defined"
     ]
    }
   ],
   "source": [
    "from selenium.webdriver.common.keys import Keys\n",
    "\n",
    "#A mensagem que quero enviar e os contatos.\n",
    "mensagem = \"\"\" Oá, tudo bem?\n",
    "Estou fazendo um teste de Automação. Não responda! \"\"\"\n",
    "\n",
    "lista_contatos = [\"Nivea Mana Love\", \"Priscila Prisgay\", \"Glauco Silva\"]\n",
    "\n",
    "#clicar na lupa\n",
    "nav.find_element('xpath', '//*[@id=\"side\"]/div[1]/div/div[2]/button/div[2]/span').click()\n",
    "#escreve na lupa\n",
    "nav.find_element('xpath', '//*[@id=\"side\"]/div[1]/div/div[2]/div[2]/div/div[1]/p').send_keys('Nivea Mana Love')\n",
    "#aperta o enter - para isso tem que importar a chave (Keys)\n",
    "nav.find_element('xpath', '//*[@id=\"side\"]/div[1]/div/div[2]/div[2]/div/div[1]/p').send_keys(keys.ENTER)"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.12.2"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 2
}
