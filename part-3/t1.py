class Elc_Device:
    telephone = 2

    @classmethod
    def c1(cls):
        return cls.telephone

    @classmethod
    def poc_qul(cls):
        return f"Telephone star is {cls.telephone}."


class Pocket_Gad(Elc_Device):
    pager = 3
    mobile = 4

    @classmethod
    def c2(cls):
        return cls.pager

    @classmethod
    def c3(cls):
        return cls.mobile

    # Elc_Device.telephone = 2.5

    @classmethod
    def poc_qul(cls):
        return f"Mobile star {cls.mobile} and Pager star {cls.pager} but Telelphone star are less {cls.telephone}."


class Phone(Pocket_Gad):
    Smart_android = 5

    @classmethod
    def poc_qul(cls):
        return f"Phone star is {cls.Smart_android} but Mobile star ({cls.mobile}), Pager star ({cls.pager}), " \
               f"Telephony star({cls.telephone}) are less. "


d1 = Elc_Device()
d1.telephone = 2.5
d2 = Pocket_Gad()
d2.mobile = 4.5
d3 = Phone()
print(d1.poc_qul(), f'But later on star is {d1.telephone}')
print(d2.poc_qul(), f'And later on mobile star is {d2.mobile}')
print(d3.poc_qul())
