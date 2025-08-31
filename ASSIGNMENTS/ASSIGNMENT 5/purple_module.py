from abc import ABC, abstractmethod

# -----------------------------
# Abstraction
# -----------------------------
class RecommendationSystem(ABC):
    @abstractmethod
    def get_personalized_recommendations(self, user):
        pass


class SkincareRecommendation(RecommendationSystem):
    def get_personalized_recommendations(self, user):
        recommendations = [
            "Apply moisturizer twice daily",
            "Use sunscreen 20 minutes before going outside",
            "Exfoliate gently twice a week"
        ]
        return "\n".join(f"{i+1}. {rec}" for i, rec in enumerate(recommendations))


class MakeupRecommendation(RecommendationSystem):
    def get_personalized_recommendations(self, user):
        recommendations = [
            "For a natural look, use light coverage foundation",
            "Choose lipsticks with moisturizing formula",
            "Try soft blush colors for daytime wear"
        ]
        return "\n".join(f"{i+1}. {rec}" for i, rec in enumerate(recommendations))



# -----------------------------
# Inheritance (Multi-level)
# -----------------------------
class Product:
    def __init__(self, name, price):
        self._name = name
        self._price = price

    def display(self):
        print(f"Product: {self._name}, Price: ₹{self._price}")


class Haircare(Product):
    def __init__(self, name, price, hair_type):
        super().__init__(name, price)
        self.hair_type = hair_type

    def special_feature(self):
        print(f"{self._name} suitable for {self.hair_type} hair.")


class Skincare(Haircare):
    def __init__(self, name, price, hair_type, spf_rating):
        super().__init__(name, price, hair_type)
        self.spf_rating = spf_rating

    def special_feature(self):
        print(f"{self._name} with SPF {self.spf_rating} protection.")


class Makeup(Skincare):
    def __init__(self, name, price, hair_type, spf_rating, palette):
        super().__init__(name, price, hair_type, spf_rating)
        self.palette = palette

    def special_feature(self):
        print(f"{self._name} available in {self.palette} palette.")


# -----------------------------
# Polymorphism
# -----------------------------
class User(ABC):
    def __init__(self, user_name):
        self._user_name = user_name

    @abstractmethod
    def get_discounts(self):
        pass


class NormalUser(User):
    def get_discounts(self):
        return "Standard discounts"


class PremiumUser(User):
    def get_discounts(self):
        return "Premium discounts and early access"


# -----------------------------
# Encapsulation
# -----------------------------
class Payment:
    def __init__(self):
        self.__payment_details = []   # private

    def add_payment_details(self, details):
        self.__payment_details.append(details)
        print("[Encapsulation] Payment method added securely.")

    def show_payment_methods(self):
        print(f"[Encapsulation] You have {len(self.__payment_details)} payment methods saved.")
