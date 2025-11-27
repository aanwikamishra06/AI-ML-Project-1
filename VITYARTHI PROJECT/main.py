import GUI
import pygame
import INPUT
import dropdown

def main():
    pygame.init()
    
    screen, bg_welcome = GUI.welcome_screen()
    bg1_personal = pygame.image.load("BG2.png").convert()
    bg2_finance = pygame.image.load("BG2.png").convert()
    
    current_screen = "welcome" 
    running = True

    #personal screen
    personal_done = False
    job_done = False
    name = ""
    age = ""
    job = ""
    salary = ""
    job_options = ["Salaried", "Self-employed", "Student", "Unemployed", "Retired"]
    job_dropdown = dropdown.drop_down(200, 260, 250, 40, job_options)

    #necessity screen
    necessity_done = False
    rent = ""
    electric = ""
    home_loan = ""
    telephone = ""
    internet = ""
    Food = ""
    Education = ""
    staitionary = ""
    clothes_necessity = ""
    daily_expences = ""
    commute = ""
    necessity_total = 0

    luxury_done = False
    lux_clothes = ""
    appliances = ""
    makeup = ""
    jewelry = ""
    outing = ""
    vehicle = ""
    luxury_total = 0

    savings_done = False
    health_insurance = ""
    mutual_fund = ""
    saving_account = ""
    stock_market = ""
    savings_total = 0

    start_button, exit_button = GUI.button_large(screen)

    while running:
        for events in pygame.event.get():
            if events.type == pygame.QUIT:
                running = False
                
            if current_screen == "welcome":
                if events.type == pygame.MOUSEBUTTONDOWN:
                    if start_button.collidepoint(events.pos):
                        current_screen = "personal"
                    elif exit_button.collidepoint(events.pos):
                        running = False
                
            elif current_screen == "personal" and personal_done:
                dropdown.working_dropdown(job_dropdown, events)

                if events.type == pygame.MOUSEBUTTONDOWN:

                    if not job_done:
                        if back_button.collidepoint(events.pos):
                            current_screen = "welcome"
                        elif start_button.collidepoint(events.pos):
                            selected = dropdown.values_dropdown(job_dropdown)
                            if selected:
                                job = selected[0]
                                job_done = True
                        elif exit_button.collidepoint(events.pos):
                            running = False

                    else:
                        if back_button.collidepoint(events.pos):
                            current_screen = "welcome"
                        elif start_button.collidepoint(events.pos):
                            current_screen = "Necessity"
                        elif exit_button.collidepoint(events.pos):
                            running = False

            elif current_screen == "Necessity" and necessity_done:
                if events.type == pygame.MOUSEBUTTONDOWN:
                    if back_button.collidepoint(events.pos):
                        current_screen = "personal"
                    elif start_button.collidepoint(events.pos):
                        current_screen = "Luxury"
                    elif exit_button.collidepoint(events.pos):
                        running = False

            elif current_screen == "Luxury" and luxury_done:
                if events.type == pygame.MOUSEBUTTONDOWN:
                    if back_button.collidepoint(events.pos):
                        current_screen = "Necessity"
                    elif start_button.collidepoint(events.pos):
                        current_screen = "Savings"
                    elif exit_button.collidepoint(events.pos):
                        running = False

            elif current_screen == "Savings" and savings_done:
                if events.type == pygame.MOUSEBUTTONDOWN:
                    if back_button.collidepoint(events.pos):
                        current_screen = "Luxury"
                    elif start_button.collidepoint(events.pos):
                        current_screen = "Summary"
                    elif exit_button.collidepoint(events.pos):
                        running = False

            elif current_screen == "Summary":
                if events.type == pygame.MOUSEBUTTONDOWN:
                    if back_button.collidepoint(events.pos):
                        current_screen = "Savings"
                    elif exit_button.collidepoint(events.pos):
                        running = False

        # WELCOME
        if current_screen == "welcome":
            screen.blit(bg_welcome, (0, 0))
            start_button, exit_button = GUI.button_large(screen)

        # PERSONAL
        elif current_screen == "personal":
            GUI.all_screen(screen, bg1_personal,"Personal info")
            
            if not personal_done:
                name = INPUT.textbox(screen, 200, 120, 250, 40, "Enter Name: ")
                age = INPUT.textbox(screen, 200, 220, 250, 40, "Enter Age: ")
                while not age.isdigit():
                    age = INPUT.textbox(screen, 200, 220, 250, 40, "Enter Age: ")

                salary = INPUT.textbox(screen, 200, 320, 250, 40, "Enter Monthly Income: ")
                while not salary.isdigit():
                    salary = INPUT.textbox(screen, 200, 320, 250, 40, "Enter Monthly Income: ")

                personal_done = True

            font = pygame.font.Font(None, 32)

            if not job_done:
                screen.blit(font.render("Job:", True, (224, 157, 148)), (200, 235))
                dropdown.draw_dropdown(screen, job_dropdown)

            if job_done:
                screen.blit(font.render(f"Name:   {name}", True, (224, 157, 148)), (200, 120))
                screen.blit(font.render(f"Age:    {age}", True, (224, 157, 148)), (200, 160))
                screen.blit(font.render(f"Job:    {job}", True, (224, 157, 148)), (200, 200))
                screen.blit(font.render(f"Monthly Income: {salary}", True, (224, 157, 148)), (200, 240))

            back_button, start_button, exit_button = GUI.button_nav(screen)

        # NECESSITY
        elif current_screen == "Necessity":
            GUI.all_screen(screen, bg2_finance,"Necessity")

            if not necessity_done:
                rent = INPUT.textbox(screen, 120, 140, 250, 30, "Rent: ")
                while not rent.isdigit():
                    rent = INPUT.textbox(screen, 120, 140, 250, 30, "Rent: ")

                electric = INPUT.textbox(screen, 450, 140, 250, 30, "Electric: ")
                while not electric.isdigit():
                    electric = INPUT.textbox(screen, 450, 140, 250, 30, "Electric: ")

                home_loan = INPUT.textbox(screen, 120, 210, 250, 30, "Home loan: ")
                while not home_loan.isdigit():
                    home_loan = INPUT.textbox(screen, 120, 210, 250, 30, "Home loan: ")

                telephone = INPUT.textbox(screen, 450, 210, 250, 30, "Telephone: ")
                while not telephone.isdigit():
                    telephone = INPUT.textbox(screen, 450, 210, 250, 30, "Telephone: ")

                internet = INPUT.textbox(screen, 120, 280, 250, 30, "Internet: ")
                while not internet.isdigit():
                    internet = INPUT.textbox(screen, 120, 280, 250, 30, "Internet: ")

                Food = INPUT.textbox(screen, 450, 280, 250, 30, "Food: ")
                while not Food.isdigit():
                    Food = INPUT.textbox(screen, 450, 280, 250, 30, "Food: ")

                Education = INPUT.textbox(screen, 120, 350, 250, 30, "Education: ")
                while not Education.isdigit():
                    Education = INPUT.textbox(screen, 120, 350, 250, 30, "Education: ")
                    
                staitionary = INPUT.textbox(screen, 120, 420, 250, 30, "Stationary: ")
                while not staitionary.isdigit():
                    staitionary = INPUT.textbox(screen, 120, 420, 250, 30, "Stationary: ")

                clothes_necessity = INPUT.textbox(screen, 450, 420, 250, 30, "Clothes (necessity): ")
                while not clothes_necessity.isdigit():
                    clothes_necessity = INPUT.textbox(screen, 450, 420, 250, 30, "Clothes (necessity): ")

                daily_expences = INPUT.textbox(screen, 120, 490, 250, 30, "Daily expenses: ")
                while not daily_expences.isdigit():
                    daily_expences = INPUT.textbox(screen, 120, 490, 250, 30, "Daily expenses: ")

                commute = INPUT.textbox(screen, 450, 490, 250, 30, "Commute: ")
                while not commute.isdigit():
                    commute = INPUT.textbox(screen, 450, 490, 250, 30, "Commute: ")

                necessity_total = (
                    int(rent) + int(electric) + int(home_loan) + int(telephone) +
                    int(internet) + int(Food) + int(Education) +
                    int(staitionary) + int(clothes_necessity) + int(daily_expences) + int(commute)
                )
                necessity_done = True

            font = pygame.font.Font(None, 32)

            total_income = int(salary) if salary.isdigit() else 0
            necessity_budget = int(total_income * 0.5)
            necessity_percent = int((necessity_total / total_income) * 100) if total_income > 0 else 0

            t1 = font.render(f"Total necessity spending: {necessity_total}", True, (224, 157, 148))
            t2 = font.render(f"Recommended 50% budget: {necessity_budget}", True, (224, 157, 148))
            t3 = font.render(f"Your necessity % of income: {necessity_percent}%", True, (224, 157, 148))

            screen.blit(t1, t1.get_rect(center=(400, 540)))
            screen.blit(t2, t2.get_rect(center=(400, 580)))
            screen.blit(t3, t3.get_rect(center=(400, 620)))

            back_button, start_button, exit_button = GUI.button_nav(screen)

        # LUXURY
        elif current_screen == "Luxury":
            GUI.all_screen(screen, bg2_finance,"Luxury")

            if not luxury_done:
                lux_clothes = INPUT.textbox(screen, 120, 140, 250, 30, "Clothes (luxury): ")
                while not lux_clothes.isdigit():
                    lux_clothes = INPUT.textbox(screen, 120, 140, 250, 30, "Clothes (luxury): ")

                appliances = INPUT.textbox(screen, 450, 140, 250, 30, "Appliances: ")
                while not appliances.isdigit():
                    appliances = INPUT.textbox(screen, 450, 140, 250, 30, "Appliances: ")

                makeup = INPUT.textbox(screen, 120, 210, 250, 30, "Makeup: ")
                while not makeup.isdigit():
                    makeup = INPUT.textbox(screen, 120, 210, 250, 30, "Makeup: ")

                jewelry = INPUT.textbox(screen, 450, 210, 250, 30, "Jewelry: ")
                while not jewelry.isdigit():
                    jewelry = INPUT.textbox(screen, 450, 210, 250, 30, "Jewelry: ")

                outing = INPUT.textbox(screen, 120, 280, 250, 30, "Outing: ")
                while not outing.isdigit():
                    outing = INPUT.textbox(screen, 120, 280, 250, 30, "Outing: ")

                vehicle = INPUT.textbox(screen, 450, 280, 250, 30, "Vehicle: ")
                while not vehicle.isdigit():
                    vehicle = INPUT.textbox(screen, 450, 280, 250, 30, "Vehicle: ")

                luxury_total = (
                    int(lux_clothes) + int(appliances) + int(makeup) +
                    int(jewelry) + int(outing) + int(vehicle)
                )
                luxury_done = True

            font = pygame.font.Font(None, 32)

            total_income = int(salary) if salary.isdigit() else 0
            luxury_budget = int(total_income * 0.3)
            luxury_percent = int((luxury_total / total_income) * 100) if total_income > 0 else 0

            L1 = font.render(f"Total luxury spending: {luxury_total}", True, (224, 157, 148))
            L2 = font.render(f"Recommended 30% budget: {luxury_budget}", True, (224, 157, 148))
            L3 = font.render(f"Your luxury % of income: {luxury_percent}%", True, (224, 157, 148))

            screen.blit(L1, L1.get_rect(center=(400, 360)))
            screen.blit(L2, L2.get_rect(center=(400, 400)))
            screen.blit(L3, L3.get_rect(center=(400, 440)))

            back_button, start_button, exit_button = GUI.button_nav(screen)

        # SAVINGS
        elif current_screen == "Savings":
            GUI.all_screen(screen, bg2_finance,"Savings")

            if not savings_done:
                health_insurance = INPUT.textbox(screen, 120, 180, 250, 30, "Health insurance: ")
                while not health_insurance.isdigit():
                    health_insurance = INPUT.textbox(screen, 120, 180, 250, 30, "Health insurance: ")

                mutual_fund = INPUT.textbox(screen, 450, 180, 250, 30, "Mutual fund: ")
                while not mutual_fund.isdigit():
                    mutual_fund = INPUT.textbox(screen, 450, 180, 250, 30, "Mutual fund: ")

                saving_account = INPUT.textbox(screen, 120, 250, 250, 30, "Saving Account: ")
                while not saving_account.isdigit():
                    saving_account = INPUT.textbox(screen, 120, 250, 250, 30, "Saving Account: ")

                stock_market = INPUT.textbox(screen, 450, 250, 250, 30, "Stock Market: ")
                while not stock_market.isdigit():
                    stock_market = INPUT.textbox(screen, 450, 250, 250, 30, "Stock Market: ")

                savings_total = (
                    int(health_insurance) + int(mutual_fund) +
                    int(saving_account) + int(stock_market)
                )
                savings_done = True

            font = pygame.font.Font(None, 32)

            total_income = int(salary) if salary.isdigit() else 0
            savings_budget = int(total_income * 0.2)
            savings_percent = int((savings_total / total_income) * 100) if total_income > 0 else 0

            S1 = font.render(f"Total savings/investment: {savings_total}", True, (224, 157, 148),(200, 120))
            S2 = font.render(f"Recommended 20% budget: {savings_budget}", True, (224, 157, 148),(200, 160))
            S3 = font.render(f"Your savings % of income: {savings_percent}%", True, (224, 157, 148),(200, 200))

            screen.blit(S1, S1.get_rect(center=(400, 360)))
            screen.blit(S2, S2.get_rect(center=(400, 400)))
            screen.blit(S3, S3.get_rect(center=(400, 440)))

            back_button, start_button, exit_button = GUI.button_nav(screen)

        # SUMMARY
        elif current_screen == "Summary":
            GUI.all_screen(screen, bg2_finance,"Summary")
            font = pygame.font.Font(None, 32)

            total_income = int(salary) if salary.isdigit() else 0
            total_expenditure = necessity_total + luxury_total + savings_total
            balance = total_income - total_expenditure

            nec_pct = int((necessity_total / total_income) * 100) if total_income > 0 else 0
            lux_pct = int((luxury_total / total_income) * 100) if total_income > 0 else 0
            sav_pct = int((savings_total / total_income) * 100) if total_income > 0 else 0

            I1 = font.render(f"Total income: {total_income}", True, (224, 157, 148))
            I2 = font.render(f"Total expenditure: {total_expenditure}", True, (224, 157, 148))
            I3 = font.render(f"Balance: {balance}", True, (224, 157, 148))

            C1 = font.render(f"Necessity: {necessity_total} ({nec_pct}%)  | Ideal 50%", True, (224, 157, 148))
            C2 = font.render(f"Luxury: {luxury_total} ({lux_pct}%)       | Ideal 30%", True, (224, 157, 148))
            C3 = font.render(f"Savings: {savings_total} ({sav_pct}%)     | Ideal 20%", True, (224, 157, 148))

            screen.blit(I1, I1.get_rect(center=(400, 120)))
            screen.blit(I2, I2.get_rect(center=(400, 160)))
            screen.blit(I3, I3.get_rect(center=(400, 200)))

            screen.blit(C1, C1.get_rect(center=(400, 260)))
            screen.blit(C2, C2.get_rect(center=(400, 300)))
            screen.blit(C3, C3.get_rect(center=(400, 340)))

            if total_income > 0:
                var_nec = 50 - nec_pct
                var_lux = 30 - lux_pct
                var_sav = 20 - sav_pct

                V1 = font.render(f"Variance Necessity (50-current): {var_nec}%", True, (224, 157, 148))
                V2 = font.render(f"Variance Luxury (30-current): {var_lux}%", True, (224, 157, 148))
                V3 = font.render(f"Variance Savings (20-current): {var_sav}%", True, (224, 157, 148))

                screen.blit(V1, V1.get_rect(center=(400, 400)))
                screen.blit(V2, V2.get_rect(center=(400, 440)))
                screen.blit(V3, V3.get_rect(center=(400, 480)))

            back_button, start_button, exit_button = GUI.button_nav(screen)
                    
        pygame.display.flip()

    pygame.quit()

main()