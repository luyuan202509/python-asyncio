def build_profile(first, last, **user_info):

    user_info['fistname'] = first
    user_info['lastname'] = last
    return user_info

if __name__ == '__main__':
    user_profile = build_profile('albert', 'einstein',location='princeton',field='physics')
    print(user_profile)
