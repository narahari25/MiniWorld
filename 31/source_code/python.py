import subprocess as sp
import pymysql
import pymysql.cursors

def hireAnAthlete():
    """
    Function to hire an athlete in the Olympics database.
    """
    try:
        # Takes athlete details as input
        row = {}
        print("Enter new athlete's details: ")
        row["name"] = input("Name: ")
        row["gender"] = input("Gender (M/F): ")
        row["dob"] = input("Date of Birth (YYYY-MM-DD): ")
        row["country_id"] = input("Country ID: ")
        row["height"] = int(input("Height: "))
        row["weight"] = int(input("Weight: "))
        row["cid"] = int(input("CID: "))
        row["sid"] = int(input("SID: "))

        query = "INSERT INTO athlete (name, gender, dob, country_id, height, weight, cid, sid) VALUES ('%s', '%s', '%s', %s, %s, %s, %s, %s)" % (
            row["name"], row["gender"], row["dob"], row["country_id"], row["height"], row["weight"], row["cid"], row["sid"])

        print(query)
        cur.execute(query)
        con.commit()

        print("Inserted into Database")

    except Exception as e:
        con.rollback()
        print("Failed to insert into database")
        print("Error:", e)

    return
def selection_athlete_by_attribute(cur, attribute_choice):
    attribute_names = {
        1: "name",
        2: "dob",
        3: "gender",
        4: "country_id",
        5: "height",
        6: "weight",
        7: "cid",
        8: "sid",
    }
    attribute_name = attribute_names.get(attribute_choice)
    attribute_value = input(f"Enter {attribute_name}: ")

    if attribute_name == "gender":
        print("Sorting options for age:")
        print("1. Normal")
        print("2. Ascending age")
        print("3. Descending age")
        sort_option = int(input("Enter sort option (1, 2, or 3): "))

        if sort_option == 1:
            query = f"SELECT * FROM athlete WHERE {attribute_name} = '{attribute_value}'"
        elif sort_option == 2:
            query = f"SELECT * FROM athlete WHERE {attribute_name} = '{attribute_value}' ORDER BY DATEDIFF(CURDATE(), dob) ASC"
        elif sort_option == 3:
            query = f"SELECT * FROM athlete WHERE {attribute_name} = '{attribute_value}' ORDER BY DATEDIFF(CURDATE(), dob) DESC"
        else:
            print("Invalid sort option")
            return

    else:
        query = (
            f"SELECT * FROM athlete WHERE {attribute_name} LIKE '%%%s%%'"
            % attribute_value
        )

    execute_and_print_query(cur, query)
    
def selection_coach_by_attribute(cur, attribute_choice):
    attribute_names = {
        1: "NAME",
        2: "gender",
        3: "expertise_in"
    }
    attribute_name = attribute_names.get(attribute_choice)
    attribute_value = input(f"Enter {attribute_name}: ")
    
    query = f"SELECT * FROM coach WHERE {attribute_name} LIKE '%%%s%%'" % attribute_value
    execute_and_print_query(cur, query)

def selection_countries_by_attribute(cur, attribute_choice):
    attribute_names = {
        1: "name",
        2: "country_code"
    }
    attribute_name = attribute_names.get(attribute_choice)
    attribute_value = input(f"Enter {attribute_name}: ")
    
    query = f"SELECT * FROM countries WHERE {attribute_name} LIKE '%%%s%%'" % attribute_value
    execute_and_print_query(cur, query)

def selection_sports_by_attribute(cur, attribute_choice):
    attribute_names = {
        1: "name",
        2: "category",
        3: "decision_makers",
        4: "record"
    }
    attribute_name = attribute_names.get(attribute_choice)
    attribute_value = input(f"Enter {attribute_name}: ")
    
    query = f"SELECT * FROM sports WHERE {attribute_name} LIKE '%%%s%%'" % attribute_value
    execute_and_print_query(cur, query)

def selection_torch_by_attribute(cur, attribute_choice):
    attribute_names = {
        1: "colour",
        2: "length",
        3: "composition",
        4: "fuel",
        5: "manufacturer"
    }
    attribute_name = attribute_names.get(attribute_choice)
    attribute_value = input(f"Enter {attribute_name}: ")
    
    query = f"SELECT * FROM torch WHERE {attribute_name} LIKE '%%%s%%'" % attribute_value
    execute_and_print_query(cur, query)

def selection_tournament_winner_by_attribute(cur, attribute_choice):
    attribute_names = {
        1: "A_ID",
        2: "T_ID",
        3: "result"
    }
    attribute_name = attribute_names.get(attribute_choice)
    attribute_value = input(f"Enter {attribute_name}: ")
    
    query = f"SELECT * FROM tournament_winner WHERE {attribute_name} = %s" % attribute_value
    execute_and_print_query(cur, query)

def selection_tournaments_by_attribute(cur, attribute_choice):
    attribute_names = {
        1: "duration",
        2: "result",
        3: "date",
        4: "S_ID",
        5: "O_ID"
    }
    attribute_name = attribute_names.get(attribute_choice)
    attribute_value = input(f"Enter {attribute_name}: ")
    
    if attribute_name == "date":
        query = f"SELECT * FROM tournaments WHERE {attribute_name} = %s" % attribute_value
    else:
        query = f"SELECT * FROM tournaments WHERE {attribute_name} LIKE '%%%s%%'" % attribute_value

    execute_and_print_query(cur, query)

def selection_ranking_by_attribute(cur, attribute_choice):
    attribute_names = {
        1: "o_id",
        2: "country_id",
        3: "rank"
    }
    attribute_name = attribute_names.get(attribute_choice)
    attribute_value = input(f"Enter {attribute_name}: ")
    
    query = f"SELECT * FROM ranking WHERE {attribute_name} = %s" % attribute_value
    execute_and_print_query(cur, query)

# Helper function to execute query and print results
def execute_and_print_query(cur, query):
    try:
        cur.execute(query)
        results = cur.fetchall()

        if results:
            print("selection results:")
            for result in results:
                print(result)
        else:
            print("No results found.")

    except pymysql.Error as e:
        print("Failed to selection in the database")
        print("MySQL Error:", e)

def insertCountry():
    """
    Function to insert a country into the Countries table.
    """
    try:
        # Takes country details as input
        row = {}
        print("Enter new country's details: ")
        row["code"] = input("Country Code: ")
        row["name"] = input("Country Name: ")
       

        query = "INSERT INTO countries (country_code, name) VALUES ('%s', '%s')" % (
            row["code"], row["name"])

        print(query)
        cur.execute(query)
        con.commit()

        print("Inserted into Database")

    except Exception as e:
        con.rollback()
        print("Failed to insert into database")
        print("Error:", e)

    return

def insertOlympicOccurrence():
    """
    Function to insert data into the OlympicOccurrence table.
    """
    try:
        # Takes OlympicOccurrence details as input
        print("Enter new OlympicOccurrence details: ")
        occurrence_id = int(input("Occurrence ID: "))
        winning_country = int(input("Winning Country ID: "))
        host_countries = input("Host Countries: ")
        year = int(input("Year: "))
        season_participated = input("Season Participated: ")

        query = "INSERT INTO OlympicOccurrence (id, winning_country, host_countries, year, season_participated) VALUES (%s, %s, %s, %s, '%s')"
        values = (occurrence_id, winning_country, host_countries, year, season_participated)

        print(query % values)
        cur.execute(query, values)
        con.commit()

        print("Inserted into Database")

    except pymysql.Error as e:
        con.rollback()
        print("Failed to insert into database")
        print("MySQL Error:", e)

    return

def insertTorch():
    """
    Function to insert data into the torch table.
    """
    try:
        # Takes torch details as input
        print("Enter new Torch details: ")
        color = input("Color: ")
        length = input("Length: ")
        composition = input("Composition: ")
        fuel = input("Fuel: ")
        manufacturer = input("Manufacturer: ")
        olympic_occurrence_id = int(input("Olympic Occurrence ID: "))

        query = "INSERT INTO torch (colour, length, composition, fuel, manufacturer, o_id) VALUES (%s, %s, %s, %s, %s, %s)"
        values = (color, length, composition, fuel, manufacturer, olympic_occurrence_id)

        print(query % values)
        cur.execute(query, values)
        con.commit()

        print("Inserted into Database")

    except pymysql.Error as e:
        con.rollback()
        print("Failed to insert into database")
        print("MySQL Error:", e)

    return

def insertAthleteMedals():
    """
    Function to insert data into the athlete_medals table.
    """
    try:
        # Takes athlete medals details as input
        print("Enter new athlete medals details: ")
        athlete_id = int(input("Athlete ID: "))
        occurrence_id = int(input("Occurrence ID: "))
        medals_received = int(input("Medals Received: "))

        query = "INSERT INTO athlete_medals (A_ID, O_ID, Medals_Received) VALUES (%s, %s, %s)"
        values = (athlete_id, occurrence_id, medals_received)

        print(query % values)
        cur.execute(query, values)
        con.commit()

        print("Inserted into Database")

    except pymysql.Error as e:
        con.rollback()
        print("Failed to insert into database")
        print("MySQL Error:", e)

    return

def insertCoach():
    """
    Function to insert data into the coach table.
    """
    try:
        # Takes coach details as input
        print("Enter new coach details: ")
        coach_id = int(input("Coach ID: "))
        name = input("Name: ")
        gender = input("Gender (M/F): ")
        expertise_in = input("Expertise In: ")

        query = "INSERT INTO coach (COACH_ID, NAME, GENDER, EXPERTISE_IN) VALUES (%s, '%s', '%s', '%s')"
        values = (coach_id, name, gender, expertise_in)

        print(query % values)
        cur.execute(query, values)
        con.commit()

        print("Inserted into Database")

    except pymysql.Error as e:
        con.rollback()
        print("Failed to insert into database")
        print("MySQL Error:", e)

    return

def insertRanking():
    """
    Function to insert data into the ranking table.
    """
    try:
        # Takes ranking details as input
        print("Enter new ranking details: ")
        occurrence_id = int(input("Occurrence ID: "))
        country_id = input("Country ID: ")
        rank = int(input("Rank: "))

        query = "INSERT INTO ranking (o_id,country_id, rank) VALUES (%s, %s, %s)"
        values = (occurrence_id, country_id, rank)

        print(query % values)
        cur.execute(query, values)
        con.commit()

        print("Inserted into Database")

    except pymysql.Error as e:
        con.rollback()
        print("Failed to insert into database")
        print("MySQL Error:", e)

    return

def genderDistribution():
    """
    Function to display gender distribution of athletes.
    """
    try:
        # Query to retrieve gender distribution
        query = "SELECT gender, COUNT(*) as count FROM athlete GROUP BY gender"
        cur.execute(query)
        result = cur.fetchall()

        # Display the results
        print("Gender Distribution:")
        for row in result:
            print(f"{row['gender']}: {row['count']} athletes")

    except pymysql.Error as e:
        print("Failed to fetch data from database")
        print("MySQL Error:", e)

    return


def averageAgeOfAthletes():
    """
    Function to calculate the average age of all athletes.
    """
    try:
        # Query to retrieve the average age
        query = "SELECT AVG(YEAR(CURDATE()) - YEAR(dob)) as average_age FROM athlete"

        cur.execute(query)
        result = cur.fetchone()

        # Display the result
        if result and result['average_age'] is not None:
            print(f"Average Age of All Athletes: {result['average_age']:.2f} years")
        else:
            print("No data available for average age of athletes")

    except pymysql.Error as e:
        print("Failed to fetch data from database")
        print("MySQL Error:", e)

    return




def Deletecountry():
    """
    Function to delete a country from the Countries table.
    """
    try:
        # Takes country code as input
        country_code = input("Enter country code to delete: ")

        query = "DELETE FROM countries WHERE country_code = %s"
        values = (country_code,)

        print(query % values)
        cur.execute(query, values)
        con.commit()

        print("Country deleted from Database")

    except pymysql.Error as e:
        con.rollback()
        print("Failed to delete country from the database")
        print("MySQL Error:", e)

    return

def DeleteAthlete():
    """
    Function to delete a country from the Countries table.
    """
    try:
        # Takes country code as input
        athlete_id = input("Enter athlete_id to delete: ")

        query = "DELETE FROM athlete WHERE athlete_id = %s"
        values = (athlete_id,)

        print(query % values)
        cur.execute(query, values)
        con.commit()

        print("Athlete deleted from Database")

    except pymysql.Error as e:
        con.rollback()
        print("Failed to delete country from the database")
        print("MySQL Error:", e)

    return

#
#   update tables
# 
def updateOlympicOccurrence():

    try:
        # Takes OlympicOccurrence details as input
        print("Enter details for OlympicOccurrence update: ")
        occurrence_id = int(input("Occurrence ID: "))
        row = {}
        row["winning_country"] = int(input("Updated Winning Country ID: "))
        row["host_countries"] = input("Updated Host Countries: ")

        query = """
            UPDATE OlympicOccurrence
            SET winning_country=%s, host_countries=%s
            WHERE id=%s
        """
        values = (row["winning_country"], row["host_countries"], occurrence_id)

        print(query % values)
        cur.execute(query, values)
        con.commit()

        print("Updated OlympicOccurrence in Database")

    except Exception as e:
        con.rollback()
        print("Failed to update OlympicOccurrence in database")
        print("Error:", e)


def updateAthlete():

    try:
        # Takes athlete details as input
        print("Enter details for athlete update: ")
        athlete_id = int(input("Athlete ID: "))
        row = {}
        row["name"] = input("Updated Name: ")
        row["gender"] = input("Updated Gender (Male/F): ")
        row["dob"] = input("Updated Date of Birth (YYYY-MM-DD): ")
        row["country_id"] = int(input("Updated Country ID: "))
        row["height"] = int(input("Updated Height: "))
        row["weight"] = int(input("Updated Weight: "))

        query = """
            UPDATE athlete
            SET name=%s, gender=%s, dob=%s, country_id=%s, height=%s, weight=%s
            WHERE athlete_id=%s
        """
        values = (row["name"], row["gender"], row["dob"], row["country_id"], row["height"], row["weight"], athlete_id)

        print(query % values)
        cur.execute(query, values)
        con.commit()

        print("Updated athlete in Database")

    except Exception as e:
        con.rollback()
        print("Failed to update athlete in database")
        print("Error:", e)

def updateAthlete_medals():
    """
    Function to update details in the athlete_medals table.
    """
    try:
        print("Enter details for athlete_medals update: ")
        athlete_id = int(input("Athlete ID: "))
        occurrence_id = int(input("Olympic Occurrence ID: "))
        medals_received = int(input("Updated Medals Received: "))

        query = """
            UPDATE athlete_medals
            SET Medals_Received=%s
            WHERE A_ID=%s AND O_ID=%s
        """
        values = (medals_received, athlete_id, occurrence_id)

        print(query % values)
        cur.execute(query, values)
        con.commit()

        print("Updated athlete_medals in Database")

    except Exception as e:
        con.rollback()
        print("Failed to update athlete_medals in database")
        print("Error:", e)


def updateCoach():
    """
    Function to update details in the coach table.
    """
    try:
        print("Enter details for coach update: ")
        coach_id = int(input("Coach ID: "))
        name = input("Updated Name: ")
        gender = input("Updated Gender (M/F): ")
        expertise_in = input("Updated Expertise In: ")

        query = """
            UPDATE coach
            SET NAME=%s, GENDER=%s, EXPERTISE_IN=%s
            WHERE COACH_ID=%s
        """
        values = (name, gender, expertise_in, coach_id)

        print(query % values)
        cur.execute(query, values)
        con.commit()

        print("Updated coach in Database")

    except Exception as e:
        con.rollback()
        print("Failed to update coach in database")
        print("Error:", e)
        
        
def updateCountries():
    """
    Function to update details in the Countries table.
    """
    try:
        # Takes country details as input
        print("Enter details for country update: ")
        country_code = int(input("Country ID: "))
        row = {}
        row["code"] = input("Updated Country Code: ")
        row["name"] = input("Updated Country Name: ")
        row["flag"] = input("Updated Country Flag: ")

        query = """
            UPDATE countries
            SET country_code=%s, name=%s, flag=%s
            WHERE country_code=%s
        """
        values = (row["code"], row["name"], row["flag"], country_code)

        print(query % values)
        cur.execute(query, values)
        con.commit()

        print("Updated country in Database")

    except Exception as e:
        con.rollback()
        print("Failed to update country in database")
        print("Error:", e)

def updateRanking():
    """
    Function to update details in the ranking table.
    """
    try:
        print("Enter details for ranking update: ")
        athlete_id = int(input("Athlete ID: "))
        rank = int(input("Updated Rank: "))
        sport_id = int(input("Sport ID: "))

        query = """
            UPDATE ranking
            SET RANK=%s
            WHERE A_ID=%s AND S_ID=%s
        """
        values = (rank, athlete_id, sport_id)

        print(query % values)
        cur.execute(query, values)
        con.commit()

        print("Updated ranking in Database")

    except Exception as e:
        con.rollback()
        print("Failed to update ranking in database")
        print("Error:", e)

def updateSports():
    """
    Function to update details in the sports table.
    """
    try:
        print("Enter details for sports update: ")
        sport_id = int(input("Sport ID: "))
        name = input("Updated Name: ")
        category = input("Updated Category: ")
        decision_makers = input("Updated Decision Makers: ")
        record = input("Updated Record: ")

        query = """
            UPDATE sports
            SET NAME=%s, CATEGORY=%s, DECISION_MAKERS=%s, RECORD=%s
            WHERE SPORT_ID=%s
        """
        values = (name, category, decision_makers, record, sport_id)

        print(query % values)
        cur.execute(query, values)
        con.commit()

        print("Updated sports in Database")

    except Exception as e:
        con.rollback()
        print("Failed to update sports in database")
        print("Error:", e)

def updateTorch():
    """
    Function to update details in the Torch table.
    """
    try:
        # Takes Torch details as input
        print("Enter details for Torch update: ")
        torch_id = int(input("Torch ID: "))
        row = {}
        row["color"] = input("Updated Color: ")
        row["length"] = float(input("Updated Length: "))
        row["composition"] = input("Updated Composition: ")
        row["fuel"] = input("Updated Fuel: ")
        row["manufacturer"] = input("Updated Manufacturer: ")
        row["olympic_occurrence_id"] = int(input("Updated Olympic Occurrence ID: "))

        query = """
            UPDATE torch
            SET colour=%s, length=%s, composition=%s, fuel=%s, manufacturer=%s, o_id=%s
            WHERE id=%s
        """
        values = (row["color"], row["length"], row["composition"], row["fuel"], row["manufacturer"], row["olympic_occurrence_id"], torch_id)

        print(query % values)
        cur.execute(query, values)
        con.commit()

        print("Updated Torch in Database")

    except Exception as e:
        con.rollback()
        print("Failed to update Torch in database")
        print("Error:", e)
def DeleteTable():
    try:
        # Display the list of tables
        print("List of Tables:")
        print("1. Countries")
        print("2. athlete")
    
        

        # Get the table choice from the user
        table_choice = int(input("Enter the number of the table to delete: "))
        
        if table_choice == 1:
            Deletecountry()
        elif table_choice == 2:
            DeleteAthlete()
        else:
            print("Invalid table choice.")

    except ValueError:
        print("Invalid input. Please enter a number.")
    except Exception as e:
        print("Error:", e)
def updateTournament_winner():
    """
    Function to update details in the tournament_winner table.
    """
    try:
        print("Enter details for tournament_winner update: ")
        tournament_id = int(input("Tournament ID: "))
        athlete_id = int(input("Athlete ID: "))
        result = int(input("Updated Result (1/0): "))

        query = """
            UPDATE tournament_winner
            SET RESULT=%s
            WHERE T_ID=%s AND A_ID=%s
        """
        values = (result, tournament_id, athlete_id)

        print(query % values)
        cur.execute(query, values)
        con.commit()

        print("Updated tournament_winner in Database")

    except Exception as e:
        con.rollback()
        print("Failed to update tournament_winner in database")
        print("Error:", e)


def updateTournaments():
    """
    Function to update details in the tournaments table.
    """
    try:
        print("Enter details for tournaments update: ")
        tournament_id = int(input("Tournament ID: "))
        duration = input("Updated Duration: ")
        result = input("Updated Result: ")
        date = input("Updated Date (YYYY-MM-DD): ")
        sport_id = int(input("Sport ID: "))
        occurrence_id = int(input("Olympic Occurrence ID: "))

        query = """
            UPDATE tournaments
            SET DURATION=%s, RESULT=%s, DATE=%s, S_ID=%s, O_ID=%s
            WHERE TOURNAMENT_ID=%s
        """
        values = (duration, result, date, sport_id, occurrence_id, tournament_id)

        print(query % values)
        cur.execute(query, values)
        con.commit()

        print("Updated tournaments in Database")

    except Exception as e:
        con.rollback()
        print("Failed to update tournaments in database")
        print("Error:", e)
        
        
def updateTable():
    """
    Function to update details in a table in the Olympics database.
    """
    try:
        # Display the list of tables
        print("List of Tables:")
        print("1. OLympicOccurrence")
        print("2. athlete")
        print("3. athlete_medals")
        print("4. coach")
        print("5. countries")
        print("6. ranking")
        print("7. sports")
        print("8. torch")
        print("9. tournament_winner")
        print("10. tournaments")
        

        # Get the table choice from the user
        table_choice = int(input("Enter the number of the table to update: "))
        
        if table_choice == 1:
            updateOlympicOccurrence()
        elif table_choice == 2:
            updateAthlete()
        elif table_choice == 3:
            updateAthlete_medals()
        elif table_choice == 4:
            updateCoach()
        elif table_choice == 5:
            updateCountries()
        elif table_choice == 6:
            updateRanking()
        elif table_choice == 7:
            updateSports()
        elif table_choice == 8:
            updateTorch()
        elif table_choice == 9:
            updateTournament_winner()
        elif table_choice == 10:
            updateTournaments()
    
        else:
            print("Invalid table choice.")

    except ValueError:
        print("Invalid input. Please enter a number.")
    except Exception as e:
        print("Error:", e)

def InsertTable():
    """
    Function to insert details in a table in the Olympics database.
    """
    try:
        # Display the list of tables
        print("List of Tables:")
        print("1. OLympicOccurrence")
        print("2. athlete")
        print("3. athlete_medals")
        print("4. coach")
        print("5. countries")
        print("6. ranking")
        print("7. torch")        

        # Get the table choice from the user
        table_choice = int(input("Enter the number of the table to insert into: "))
        
        if table_choice == 1:
            insertOlympicOccurrence()
        elif table_choice == 2:
            hireAnAthlete()
        elif table_choice == 3:
            insertAthleteMedals()
        elif table_choice == 4:
            insertCoach()
        elif table_choice == 5:
            insertCountry()
        elif table_choice == 6:
            insertRanking()
        elif table_choice == 7:
            insertTorch()
    
        else:
            print("Invalid table choice.")

    except ValueError:
        print("Invalid input. Please enter a number.")
    except Exception as e:
        print("Error:", e)

def Searchathlete():
    try:
        # Takes the first 3 letters of the athlete's name as input
        name = input("Enter the search text of the athlete's name: ")

        # Construct the SQL query for partial text match
        query = "SELECT * FROM athlete WHERE name LIKE %s"
        name_pattern = f"{name}%"

        # Execute the query
        cur.execute(query, (name_pattern,))
        result = cur.fetchall()

        # Print the matching athletes
        if result:
            print("Matching Athletes:")
            for row in result:
                print(row)
        else:
            print("No matching athletes found.")

    except pymysql.Error as e:
        print("Failed to execute the search query")
        print("MySQL Error:", e)

    return

def Searchsport():
    try:
        # Takes the first 3 letters of the athlete's name as input
        name = input("Enter the search text of the sport's name: ")

        # Construct the SQL query for partial text match
        query = "SELECT * FROM sports WHERE name LIKE %s"
        name_pattern = f"{name}%"

        # Execute the query
        cur.execute(query, (name_pattern,))
        result = cur.fetchall()

        # Print the matching athletes
        if result:
            print("Matching sports:")
            for row in result:
                print(row)
        else:
            print("No matching sports found.")

    except pymysql.Error as e:
        print("Failed to execute the search query")
        print("MySQL Error:", e)

    return

def Searchtable():
    try:
        # Display the list of tables
        print("List of Tables:")
        print("1. Athelete Name")
        print("2. Sport Name")
    
        

        # Get the table choice from the user
        table_choice = int(input("Enter the number of the table to Search: "))
        
        if table_choice == 1:
            Searchathlete()
        elif table_choice == 2:
            Searchsport()
        else:
            print("Invalid table choice.")

    except ValueError:
        print("Invalid input. Please enter a number.")
    except Exception as e:
        print("Error:", e)



def Selectiontable():
    try:
                print("1. selection Athlete")
                print("2. selection Coach")
                print("3. selection Countries")
                print("4. selection Sports")
                print("5. selection Torch")
                print("6. selection Tournament Winner")
                print("7. selection Tournaments")
                print("8. selection Ranking")
                print("9. Exit")
                choice = int(input("Enter choice: "))

                if 1 <= choice <= 8:
                    tmp = sp.call('clear', shell=True)
                    # Execute the corresponding selection function
                    if choice == 1:
                        # Present the list of attributes for the chosen entity
                        print("Choose attribute to selection:")
                        print("1. Name")
                        print("2. Date of Birth")
                        print("3. Gender")
                        print("4. Country ID")
                        print("5. Height")
                        print("6. Weight")
                        print("7. Coach ID")
                        print("8. Sport ID")
                        attribute_choice = int(input("Enter attribute choice: "))
                        selection_athlete_by_attribute(cur, attribute_choice)
                    elif choice == 2:
                        print("Choose attribute to selection:")
                        print("1. Name")
                        print("2. Gender")
                        print("3. Expertise In")
                        attribute_choice = int(input("Enter attribute choice: "))
                        selection_coach_by_attribute(cur, attribute_choice)
                    elif choice == 3:
                        print("Choose attribute to selection:")
                        print("1. Name")
                        print("2. Flag")
                        attribute_choice = int(input("Enter attribute choice: "))
                        selection_countries_by_attribute(cur, attribute_choice)
                    elif choice == 4:
                        print("Choose attribute to selection:")
                        print("1. Name")
                        print("2. Category")
                        print("3. Decision Makers")
                        print("4. Record")
                        attribute_choice = int(input("Enter attribute choice: "))
                        selection_sports_by_attribute(cur, attribute_choice)
                    elif choice == 5:
                        print("Choose attribute to selection:")
                        print("1. Colour")
                        print("2. Length")
                        print("3. Composition")
                        print("4. Fuel")
                        print("5. Manufacturer")
                        attribute_choice = int(input("Enter attribute choice: "))
                        selection_torch_by_attribute(cur, attribute_choice)
                    elif choice == 6:
                        print("Choose attribute to selection:")
                        print("1. Athlete ID")
                        print("2. Tournament ID")
                        print("3. Result")
                        attribute_choice = int(input("Enter attribute choice: "))
                        selection_tournament_winner_by_attribute(cur, attribute_choice)
                    elif choice == 7:
                        print("Choose attribute to selection:")
                        print("1. Duration")
                        print("2. Result")
                        print("3. Date")
                        print("4. Sport ID")
                        print("5. Olympic ID")
                        attribute_choice = int(input("Enter attribute choice: "))
                        selection_tournaments_by_attribute(cur, attribute_choice)
                    elif choice == 8:
                        print("Choose attribute to selection:")
                        print("1. Olympic ID")
                        print("2. Country ID")
                        print("3. Rank")
                        attribute_choice = int(input("Enter attribute choice: "))
                        selection_ranking_by_attribute(cur, attribute_choice)
                else:
                    print("Error: Invalid Option")

            

    except Exception as e:
        tmp = sp.call('clear', shell=True)
        print(e)
        print("Error occurred during the operation")

def summedals():
    try:
        # Input: Country ID
        country_id = input("Enter Country ID: ")

        # Construct the SQL query
        query = """
            SELECT a.country_id, SUM(am.Medals_Received) AS Total_Medals
            FROM athlete AS a
            JOIN athlete_medals AS am ON a.athlete_id = am.A_ID
            WHERE a.country_id = %s
            GROUP BY a.country_id
        """

        # Execute the query
        cur.execute(query, (country_id,))
        result = cur.fetchone()

        # Print the result
        if result:
            print(f"Total Medals for Country {country_id}: {result['Total_Medals']}")
        else:
            print(f"No medals found for Country {country_id}.")

    except pymysql.Error as e:
        print("Failed to execute the query")
        print("MySQL Error:", e)

    return
def Minmedals():
    try:
        # Construct the SQL query
        query = """
        SELECT
            a.athlete_id,
            a.name,
            a.dob,
            a.gender,
            a.country_id,
            a.height,
            a.weight,
            a.cid,
            a.sid,
            COALESCE(SUM(am.Medals_Received), 0) AS total_medals
        FROM
            athlete a
        LEFT JOIN
            athlete_medals am ON a.athlete_id = am.A_ID
        GROUP BY
            a.athlete_id, a.name, a.dob, a.gender, a.country_id, a.height, a.weight, a.cid, a.sid
        HAVING
            COALESCE(SUM(am.Medals_Received), 0) = (
                SELECT MIN(total_medals)
                FROM (
                    SELECT COALESCE(SUM(Medals_Received), 0) AS total_medals
                    FROM athlete_medals
                    GROUP BY A_ID
                ) AS subquery
            );

        """

        # Execute the query
        cur.execute(query)
        results = cur.fetchall()

        # Print the results
        if results:
            print("Athletes with Minimum Medals:")
            for result in results:
                print(f"Athlete ID: {result['athlete_id']}")
                print(f"Country ID: {result['country_id']}")
                print(f"Total Medals: {result['total_medals']}\n")
        else:
            print("No athletes found.")

    except pymysql.Error as e:
        print("Failed to execute the query")
        print("MySQL Error:", e)

    return


def Maxmedals():
    try:
        # Construct the SQL query
        query = """
        SELECT
            a.athlete_id,
            a.name,
            a.dob,
            a.gender,
            a.country_id,
            a.height,
            a.weight,
            a.cid,
            a.sid,
            COALESCE(SUM(am.Medals_Received), 0) AS total_medals
        FROM
            athlete a
        LEFT JOIN
            athlete_medals am ON a.athlete_id = am.A_ID
        GROUP BY
            a.athlete_id, a.name, a.dob, a.gender, a.country_id, a.height, a.weight, a.cid, a.sid
        HAVING
            COALESCE(SUM(am.Medals_Received), 0) = (
                SELECT MAX(total_medals)
                FROM (
                    SELECT COALESCE(SUM(Medals_Received), 0) AS total_medals
                    FROM athlete_medals
                    GROUP BY A_ID
                ) AS subquery
            );

        """

        # Execute the query
        cur.execute(query)
        results = cur.fetchall()

        # Print the results
        if results:
            print("Athletes with Minimum Medals:")
            for result in results:
                print(f"Athlete ID: {result['athlete_id']}")
                print(f"Country ID: {result['country_id']}")
                print(f"Total Medals: {result['total_medals']}\n")
        else:
            print("No athletes found.")

    except pymysql.Error as e:
        print("Failed to execute the query")
        print("MySQL Error:", e)

    return


def getCountriesByRank():
    """
    Function to get names of countries based on rank in a particular occurrence ID.
    """
    try:
        # Takes input for occurrence ID and rank
        occurrence_id = int(input("Enter Occurrence ID: "))
        rank_threshold = int(input("Enter Rank Threshold: "))

        print("1. Countries with rank greater than a certain threshold")
        print("2. Countries with rank less than a certain threshold")
        sub_option = int(input("Enter Sub-option (1 or 2): "))

        if sub_option == 1:
            operator = ">"
        elif sub_option == 2:
            operator = "<"
        else:
            print("Invalid Sub-option")
            return
        
        values = (occurrence_id, rank_threshold)

        # Adjusted SQL query with proper table aliases and conditions
        query = """
          SELECT c.name AS country_name, r.rank
          FROM countries AS c
          INNER JOIN ranking AS r ON c.country_code = r.country_id
          WHERE r.o_id = %s AND r.rank {} %s
        """.format(operator)

        cur.execute(query, values)
        result = cur.fetchall()

        # Display the results
        print(
            f"Countries with rank {operator} {rank_threshold} in Occurrence ID {occurrence_id}:"
        )
        for row in result:
            print(f"Country: {row['country_name']}, Rank: {row['rank']}")

    except pymysql.Error as e:
        print("Failed to fetch data from the database")
        print("MySQL Error:", e)

    return
def dispatch(ch):
    """
    Function that maps helper functions to the option entered
    """
    if ch == 1:
        InsertTable()
    elif ch == 2:
        DeleteTable()
    elif ch == 3:
        genderDistribution()
    elif ch == 4:
        averageAgeOfAthletes()
    elif ch == 5:
        updateTable()
    elif ch == 6:
        Selectiontable()
    elif ch == 7:
        Searchtable()
    elif ch == 8:
        summedals()
    elif ch == 9:
        Minmedals()
    elif ch == 10:
        Maxmedals()
    elif ch == 11:
        getCountriesByRank()
    else:
        print("Error: Invalid Option")

# Global
while True:
    tmp = sp.call('clear', shell=True)
    username = "root"
    password = "V@14"

    try:
        con = pymysql.connect(
            host='localhost',
            port=3306,
            user=username,
            password=password,
            db='db',
            cursorclass=pymysql.cursors.DictCursor
        )
        tmp = sp.call('clear', shell=True)

        if con.open:
            print("Connected")
        else:
            print("Failed to connect")

        tmp = input("Enter any key to CONTINUE>")

        with con.cursor() as cur:
            while True:
                tmp = sp.call('clear', shell=True)
                print("1. Insert")
                print("2. Delete")
                print("3. gender distribution")
                print("4. average age of athletes")
                print("5. Update")
                print("6. Selection")
                print("7. Search")
                print("8. SUM of medals")
                print("9. Minimum medals")
                print("10. Maximum medals")
                print("11.Get country ranking")
                print("12. Logout")
                ch = int(input("Enter choice> "))
                tmp = sp.call('clear', shell=True)
                if ch == 12:
                    exit()
                else:
                    dispatch(ch)
                    tmp = input("Enter any key to CONTINUE>")

    except Exception as e:
        tmp = sp.call('clear', shell=True)
        print(e)
        print("Connection Refused: Either username or password is incorrect or the user doesn't have access to the database")
        tmp = input("Enter any key to CONTINUE>")
