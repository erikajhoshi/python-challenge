{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 511,
   "id": "ca482594-185f-44b7-873c-04b5170d9f4f",
   "metadata": {},
   "outputs": [],
   "source": [
    "import os\n",
    "import csv\n",
    "\n",
    "Total_Month = 0\n",
    "Total = 0\n",
    "Amount_Change = []\n",
    "Average_Change = []\n",
    "Increase = 0\n",
    "Decrease = 0\n",
    "Greatest_Increase_Month = []\n",
    "Greatest_Decrease_Month = []"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 512,
   "id": "50928f03-2e6b-4712-aa91-fd48316d0ad5",
   "metadata": {},
   "outputs": [],
   "source": [
    "userhome = os.path.expanduser('~')\n",
    "csvpath = os.path.join(userhome, 'Desktop', 'python-challenge', 'PyBank', 'Resources', 'budget_data.csv')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 513,
   "id": "39ba5179-63df-4fe5-a32d-692227a72f46",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "CSV Header: ['Date', 'Profit/Losses']\n"
     ]
    }
   ],
   "source": [
    "with open(csvpath, newline='') as csvfile:\n",
    "    csvreader = csv.reader(csvfile, delimiter=',')\n",
    "    csv_header = next(csvreader)\n",
    "    print(f\"CSV Header: {csv_header}\")\n",
    "    row = next(csvreader)\n",
    "    \n",
    "    previous_row = int(row[1])\n",
    "    Total_Month += 1\n",
    "    Total += int(row[1])\n",
    "    Increase = int(row[1])\n",
    "    Decrease = int(row[1])\n",
    "    \n",
    "    for row in csvreader:\n",
    "        Total_Month += 1\n",
    "        Total += int(row[1])\n",
    "        Total_Amount_Change = int(row[1]) - previous_row\n",
    "        Amount_Change.append(Total_Amount_Change)\n",
    "        Average_Change = sum(Amount_Change)/len(Amount_Change)\n",
    "        previous_row = int(row[1])\n",
    "        month_count.append(row[1])\n",
    "        \n",
    "        Average_Change = \"${:,.2f}\".format(Average_Change)\n",
    "      \n",
    "        \n",
    "        if int(row[1]) > Increase:\n",
    "            Increase = int(row[1])\n",
    "            Greatest_Increase_Month = str(row[0])\n",
    "            Greatest_Increase_In_Profits = Increase \n",
    "        \n",
    "        if int(row[1]) < Decrease:\n",
    "            Decrease = int(row[1])\n",
    "            Greatest_Decrease_Month = str(row[0])\n",
    "            Greatest_Decrease_In_Profits = Decrease "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 514,
   "id": "ff25fff1-97d8-4971-a35d-5b9ccf877862",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "86\n"
     ]
    }
   ],
   "source": [
    "print(Total_Month)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 515,
   "id": "3fa2b655-9b87-4dac-88fe-b9e3271b39f2",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "$-2,315.12\n"
     ]
    }
   ],
   "source": [
    "print(Average_Change)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 516,
   "id": "8f05a0e3-ff60-4216-9ceb-6948fbd2e4f0",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "1170593\n"
     ]
    }
   ],
   "source": [
    "print(Greatest_Increase_In_Profits)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 517,
   "id": "cfe6dccd-6731-4f4a-9d6c-7428d99556be",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "38382578\n"
     ]
    }
   ],
   "source": [
    "print(Total)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 518,
   "id": "784fd345-130d-4db2-8611-37de828ae3dd",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Feb-2012\n"
     ]
    }
   ],
   "source": [
    "print(Greatest_Increase_Month)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 519,
   "id": "0b996caf-8f8b-4d49-bf25-fd871792c1b7",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Sep-2013\n"
     ]
    }
   ],
   "source": [
    "print(Greatest_Decrease_Month)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 520,
   "id": "cfc71083-1c00-43f0-92c5-495f0e9027f3",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "-1196225\n"
     ]
    }
   ],
   "source": [
    "print(Greatest_Decrease_In_Profits)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 521,
   "id": "6af376a7-b3cd-43ba-8233-0cd4f4ac6346",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Financial Analysis\n",
      "-------------------------\n",
      "Total_Month: 86\n",
      "Total: $38382578\n",
      "Average_Change: $-2,315.12\n",
      "Greatest_Increase_In_Profits: Feb-2012 $1170593\n",
      "Greatest_Decrease_In_Profits: Sep-2013 $-1196225\n"
     ]
    }
   ],
   "source": [
    "print(f\"Financial Analysis\")\n",
    "print(f\"-------------------------\")\n",
    "print(f\"Total_Month: {Total_Month}\")\n",
    "print(f\"Total: ${Total}\")\n",
    "print(f\"Average_Change: {Average_Change}\")\n",
    "print(f\"Greatest_Increase_In_Profits: {Greatest_Increase_Month} ${Greatest_Increase_In_Profits}\")\n",
    "print(f\"Greatest_Decrease_In_Profits: {Greatest_Decrease_Month} ${Greatest_Decrease_In_Profits}\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 524,
   "id": "de30d90c-23cd-4686-8c10-889487a72bda",
   "metadata": {},
   "outputs": [],
   "source": [
    "final_analysis = os.path.join(userhome, 'Desktop', 'python-challenge', 'PyBank', 'Analysis', 'final_analysis.text')\n",
    "with open(final_analysis, 'w',) as txtfile:\n",
    "    txtfile.write(f\"Financial Analysis\\n\")\n",
    "    txtfile.write(f\"Total_Month: {Total_Month}\\n\")\n",
    "    txtfile.write(f\"Total: ${Total}\\n\")\n",
    "    txtfile.write(f\"Average_Change: {Average_Change}\\n\")\n",
    "    txtfile.write(f\"Greatest_Increase_In_Profits: {Greatest_Increase_Month} ${Greatest_Increase_In_Profits}\\n\")\n",
    "    txtfile.write(f\"Greatest_Decrease_In_Profits: {Greatest_Decrease_Month} ${Greatest_Decrease_In_Profits}\\n\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "1157c1cc-90bc-47c2-81d8-df724cb24f67",
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
