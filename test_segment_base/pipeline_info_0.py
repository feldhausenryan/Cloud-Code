################################################################################
# Utility functions.
################################################################################
def get_tvtk_dataset_name(dataset):
    """Given a TVTK dataset `dataset` return the string dataset type of
    the dataset.
    """
    result = 'none'
    if hasattr(dataset, 'is_a'):
        if dataset.is_a('vtkStructuredPoints') or \
           dataset.is_a('vtkImageData'):
               result = 'image_data'
        elif dataset.is_a('vtkRectilinearGrid'):
            result = 'rectilinear_grid'
        elif dataset.is_a('vtkPolyData'):
            result = 'poly_data'
        elif dataset.is_a('vtkStructuredGrid'):
            result = 'structured_grid'
        elif dataset.is_a('vtkUnstructuredGrid'):
            result = 'unstructured_grid'
        else:
            result = 'none'
    else:
        result = 'none'
    return result
