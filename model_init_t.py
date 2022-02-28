if __name__ == '__main__':

    import os
    from logging_util.logger import ProLogger
    main_path = os.path.dirname(os.path.abspath(__file__))
    pkl_path = os.path.join(main_path,'model_func_dict_global.pkl')

    proLogger = ProLogger('peano_server_app')
    proLogger.logger.info('===== start peano ===')

    def get_model_func_dict_global(pkl_path):
        import pickle
        if os.path.exists(pkl_path):
            try:
                with open(pkl_path, 'rb') as f:
                    model_func_dict_global = pickle.loads(f.read())
            except:
                proLogger.logger.info('pickle.loads except:[{}]'.format(pkl_path))
                # model_func_dict_global = peano_model_func_init()
                model_func_dict_global = {'k': 'v'}
                with open(pkl_path, 'wb') as f:
                    f.write(pickle.dumps(model_func_dict_global))
        else:
            # model_func_dict_global = peano_model_func_init()
            model_func_dict_global = {'k':'v'}
            with open(pkl_path, 'wb') as f:
                f.write(pickle.dumps(model_func_dict_global))

        proLogger.logger.info('init model_func_dict_global ok')
        proLogger.logger.info(str(model_func_dict_global))

        return model_func_dict_global

    model_func_dict_global = get_model_func_dict_global(pkl_path)