{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 213,
   "id": "4508a74e-7dfe-44b6-9e07-d750789d17d5",
   "metadata": {},
   "outputs": [],
   "source": [
    "import os\n",
    "import csv\n",
    "\n",
    "Total_Votes = 0\n",
    "Khan = 0\n",
    "Correy = 0\n",
    "Li = 0\n",
    "O_Tooley = 0\n",
    "Winner = []"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 214,
   "id": "9a0bff57-d575-4d66-a11b-cde5a091431a",
   "metadata": {},
   "outputs": [],
   "source": [
    "userhome = os.path.expanduser('~')\n",
    "csvpath = os.path.join(userhome, 'Desktop', 'python-challenge', 'pypoll', 'Resources', 'election_data.csv')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 215,
   "id": "df5a5b39-021e-431e-939e-e4ebc7a6052c",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "CSV Header: ['Voter ID', 'County', 'Candidate']\n"
     ]
    }
   ],
   "source": [
    "with open(csvpath, newline='') as csvfile:\n",
    "    csvreader = csv.reader(csvfile, delimiter=',')\n",
    "    csv_header = next(csvreader)\n",
    "    print(f\"CSV Header: {csv_header}\")\n",
    "    \n",
    "    row = next(csvreader)\n",
    "    \n",
    "    for row in csvreader:\n",
    "        Total_Votes += 1\n",
    "        \n",
    "        if (row[2] == \"Khan\"):\n",
    "            Khan += 1\n",
    "        elif (row[2] == \"Correy\"):\n",
    "            Correy += 1\n",
    "        elif (row[2] == \"Li\"):\n",
    "            Li += 1\n",
    "        else:\n",
    "            O_Tooley += 1\n",
    "    \n",
    "    Khan_Percentage = Khan / Total_Votes\n",
    "    Correy_Percentage = Correy / Total_Votes\n",
    "    Li_Percentage = Li / Total_Votes\n",
    "    O_Tooley_Percentage = O_Tooley / Total_Votes\n",
    "    Khan_Percentage = \"{:.0%}\".format(Khan_Percentage)\n",
    "    Correy_Percentage = \"{:.0%}\".format(Correy_Percentage)\n",
    "    Li_Percentage = \"{:.0%}\".format(Li_Percentage)\n",
    "    O_Tooley_Percentage = \"{:.0%}\".format(O_Tooley_Percentage)\n",
    "    \n",
    "    winner = max(Khan, Correy, Li, O_Tooley)\n",
    "    if winner == Khan:\n",
    "        Winner = \"Khan\"\n",
    "    elif winner == Correy:\n",
    "        Winner == \"Correy\"\n",
    "    elif winner == Li:\n",
    "        Winner == \"Li\"\n",
    "    else:\n",
    "        Winner == \"O_Tooley\"\n",
    "    \n",
    "        \n",
    "\n",
    "\n",
    "        "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 216,
   "id": "3d7eff13-74ca-491f-ac38-a1105bee147b",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "3521000\n"
     ]
    }
   ],
   "source": [
    "print(Total_Votes)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 217,
   "id": "f9a62ad2-120e-45e0-aa97-5e5d5a8fe14d",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "63%\n"
     ]
    }
   ],
   "source": [
    "print(Khan_Percentage)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 218,
   "id": "31f9676e-f96f-44b6-9237-7d2b4b003639",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "20%\n"
     ]
    }
   ],
   "source": [
    "print(Correy_Percentage)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 219,
   "id": "6c880d7a-cd50-4106-a3bd-5dc35b08e24b",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "14%\n"
     ]
    }
   ],
   "source": [
    "print(Li_Percentage)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 220,
   "id": "919af131-13e2-46a8-aaed-cb25e288e727",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "3%\n"
     ]
    }
   ],
   "source": [
    "print(O_Tooley_Percentage)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 221,
   "id": "d931a5fb-d737-440e-8aa8-a387d73a5a00",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Khan\n"
     ]
    }
   ],
   "source": [
    "print(Winner)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 222,
   "id": "35e421d6-da7f-4c4a-9fe4-34ccd84ed4fa",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Election_Results\n",
      "-------------------------\n",
      "Total_Votes = 3521000\n",
      "Khan: 63%(2218230)\n",
      "Correy: 20%(704200)\n",
      "Li: 14%(492940)\n",
      "O_Tooley: 3%(105630)\n",
      "-------------------------\n",
      "Winner: Khan\n"
     ]
    }
   ],
   "source": [
    "print(f\"Election_Results\")\n",
    "\n",
    "print(f\"-------------------------\")\n",
    "\n",
    "print(f\"Total_Votes = {Total_Votes}\")\n",
    "print(f\"Khan: {Khan_Percentage}({Khan})\")\n",
    "print(f\"Correy: {Correy_Percentage}({Correy})\")\n",
    "print(f\"Li: {Li_Percentage}({Li})\")\n",
    "print(f\"O_Tooley: {O_Tooley_Percentage}({O_Tooley})\")\n",
    "print(f\"-------------------------\")\n",
    "\n",
    "print(f\"Winner: {Winner}\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 223,
   "id": "beca497a-cb88-4fbf-9134-9d69c3f2b5d7",
   "metadata": {},
   "outputs": [],
   "source": [
    "final_analysis = os.path.join(userhome, 'Desktop', 'python-challenge', 'PyPoll', 'Analysis', 'final_analysis.text')\n",
    "\n",
    "with open(final_analysis, 'w',) as txtfile:\n",
    "    txtfile.write(f\"Election_Results\\n\")\n",
    "    txtfile.write(f\"Total_Votes: {Total_Votes}\\n\")\n",
    "    txtfile.write(f\"Khan: {Khan_Percentage:.3}({Khan})\")\n",
    "    txtfile.write(f\"Correy: {Correy_Percentage:.3}({Correy})\")\n",
    "    txtfile.write(f\"Li: {Li_Percentage:.3}({Li})\")\n",
    "    txtfile.write(f\"O_Tooley: {O_Tooley_Percentage:.3}({O_Tooley})\")\n",
    "    txtfile.write(f\"Winner: {Winner}\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "ad222165-ad4c-4651-b989-c034848cddcd",
   "metadata": {},
   "outputs": [],
   "source": []
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
   "version": "3.8.8"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
