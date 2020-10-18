
import numpy as np

class Gaussian_Convolution(object):
    
    def __init__(self, oscillators_map, fwhm) -> None:
        self.__osc_map = oscillators_map
        self.__std_wn = fwhm
        self.__spcetrum = {}
    
    @staticmethod
    def make_gaussian(wave_n_i, f_i, start_wl, end_wl, resolution, std_wn) -> list:
        A = 1.30062974 * np.power(10, 8)
        epslon_array = []
        for wl in np.arange(start_wl, end_wl, resolution):
            if wl == 0.0:
                epslon_array.append(0.0)
                continue
            wave_n = 1 / wl
            exp_value = (wave_n - wave_n_i) / std_wn
            epslon = (A * f_i / std_wn) * np.exp(- np.power(exp_value, 2))
            epslon_array.append(epslon)
        return epslon_array

    @staticmethod
    def sum_arrays(arrays_to_sum) -> list:
        final_guassian = arrays_to_sum[0]
        for i in range(1, len(arrays_to_sum)):
            for j in range(arrays_to_sum):
                final_guassian[j] += arrays_to_sum[i][j]
        return final_guassian
                
    def make_spectrum(self, start_wl, end_wl, n_points) -> None:
        self.gaussians = []
        resolution = (end_wl - start_wl)/n_points
        for wl_i, f_i_list in self.__osc_map.items():
            for f_i in f_i_list:
                eps_array = Gaussian_Convolution.make_gaussian(wl_i, f_i, start_wl, end_wl, resolution, self.__std_wn)
                self.gaussians.append(eps_array)
                
        eps_final = self.sum_arrays(self.gaussians)
        self.__spectrum.clear()
        wl_s = []
        for wl in np.arange(start_wl, end_wl, resolution):
            wl_s.append(wl)
        for i in range(wl_s):
            self.__spectrum.update({wl_s[i] : eps_final[i]})
    
    def write_spectrum(self, file_to_write):
        file_target_gauss = open(file_to_write + "_spectrum.dat", "w")
        sorted_keys = sorted(self.__spectrum.keys())

        for wl in sorted_keys:
            file_target_gauss.write("%10.2f %35.5f\n" %(wl, self.__spectrum[wl]))
        file_target_gauss.close()

        file_to_write_lits = open(file_to_write + "_rawData.dat", "w")

        for wl_ref in self.osc_map.keys():
            for f_ref in self.osc_map[wl_ref]:
                file_to_write_lits.write("%10.5f %10.5f\n" %(wl_ref, f_ref))
        file_to_write_lits.close()
            
    @property
    def spectrum(self):
        return self.__spcetrum
    
    

            
            